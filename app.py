import ipaddress
import json
from datetime import datetime
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)


@app.route('/block/ips/', methods = ['GET'])
def ips():
    with open('ip_block_list.json', 'r') as f:
        blocks = json.load(f)
        return jsonify(blocks)


@app.route('/block/ip/<ip>', methods = ['POST', 'DELETE'])
def ip(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return jsonify({'status_code':406,'message':'Input value is not a valid IP address'})
        # Need to return an error page here

    if request.method == 'POST':
        # Load JSON data
        try:
            with open('ip_block_list.json') as f:
                blocks = json.load(f)
        except:
            return jsonify({'status_code':500,'message':'Failed to read block file'})

        date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        # Create or update key values
        if ip in blocks.keys():
            blocks[ip]['count'] = blocks[ip]['count'] + 1 
            blocks[ip]['date'] = date_time
        else:
            blocks[ip] = {
                'count':1,
                'date':date_time
            }
    
        # Write the dictionary back to the file
        try:
            with open('ip_block_list.json', 'w') as outfile:
                json.dump(blocks, outfile)
        except:
            return jsonify({'status_code':500,'message':'Failed to save block file'})    
        
        return jsonify({'status_code':200,'message':'ok'})

    elif request.method == 'DELETE':

        # Load JSON data
        try:
            with open('ip_block_list.json') as f:
                blocks = json.load(f)
        except:
            return jsonify({'status_code':500,'message':'Failed to read block file'})
        
        # Locate and reove the entry
        if ip in blocks.keys():
            blocks.pop(ip)
        else:
            return jsonify({'status_code':201,'message':'ok'})

        # Write the dictionary back to the file
        try:
            with open('ip_block_list.json', 'w') as outfile:
                json.dump(blocks, outfile)
        except:
            return jsonify({'status_code':500,'message':'Failed to save block file'})    
        
        return jsonify({'status_code':200,'message':'ok'})      

    else:
        return jsonify({'status_code':405,'message':'Method not allowed'})


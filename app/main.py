from flask import Flask, request, jsonify
from services.vapi import create_agent_vapi
from services.retell import create_agent_retell
from schemas import CreateAgentRequest, CreateAgentResponse

app = Flask(__name__)

@app.route('/create-agent', methods=['POST'])
def create_agent():
    try:
        # Parse and validate input
        data = request.get_json()
        create_request = CreateAgentRequest(**data)
        
        # Route to correct API based on 'provider'
        if create_request.provider == 'vapi':
            response = create_agent_vapi(create_request.token, create_request.agent_config.dict())
        elif create_request.provider == 'retell':
            response = create_agent_retell(create_request.token, create_request.agent_config.dict())
        else:
            return jsonify({"error": "Invalid provider specified"}), 400
        
        # Standardize output response
        create_response = CreateAgentResponse(
            agent_id=response["agent_id"],
            provider=create_request.provider,
            message=response["message"]
        )
        return jsonify(create_response.dict()), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

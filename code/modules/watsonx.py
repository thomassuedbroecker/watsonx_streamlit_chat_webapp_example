from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
import json

class WatsonxAI():
    
    def __init__(self, 
                 apikey, 
                 region, 
                 project_id):

        self.project_id = project_id
        self.credentials = Credentials(
        url = f"https://{region}.ml.cloud.ibm.com",
        api_key = f"{apikey}",
        )

        self.client = APIClient( self.credentials)
    
    def getLLMresponse( self, messages, 
                        model_id ):
        
        model = ModelInference(
          model_id= model_id,
          api_client= self.client,
          project_id= self.project_id,
          params = {"max_new_tokens": 500 })
        
        print(f"\n***LOG messages:\n\n{messages}\n\n")
        messages_text = json.dumps(messages)
        print(f"\n***LOG messages_text:\n\n{messages_text}\n\n")

        generate_result = model.generate(messages_text)
        print(f"\n***LOG full generate_result:\n\n{generate_result}\n\n")
        
        return str(generate_result['results'][0]['generated_text'])
    
    def getLLMStreamResponse( self, messages, 
                                  model_id ):
        
        model = ModelInference(
          model_id= model_id,
          api_client= self.client,
          project_id= self.project_id,
          params = {"max_new_tokens": 500 })
        messages_text = json.dumps(messages)
        
        print(f"\n***LOG model_id:\n\n{model_id}\n\n")
        print(f"\n***LOG messages_text:\n\n{messages_text}\n\n")
        
        stream_response = model.generate_text_stream(messages_text)
        print(f"\n***LOG messages_text:\n\n{stream_response}\n\n")
        
        return stream_response

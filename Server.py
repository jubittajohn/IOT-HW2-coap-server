import os 
import aiocoap
import aiocoap.resource as resource
import asyncio
import logging

HOST_NAME = 'localhost'
PORT_NUMBER = 5683
logging.basicConfig(level=logging.INFO)

class FileServer(resource.Resource):


    async def render_put(self, request):
        try:
            filename = request.payload.decode('utf-8')
            filepath = os.path.join('DataFiles', filename)
            if os.path.exists(filepath):
                with open(filepath, 'rb') as file:
                    data = file.read()
                    return aiocoap.Message(code=aiocoap.CONTENT, payload=data)
            
            else:
                return aiocoap.Message(code= aiocoap.numbers.codes.Code.NOT_FOUND)

        except Exception as e:
            print(e)
            return aiocoap.Message(aiocoap.numbers.codes.Code.INTERNAL_SERVER_ERROR, "Internal Server Error") 

def main():

    root = resource.Site()
    root.add_resource(('.well-known', 'core'), resource.WKCResource(root.get_resources_as_linkheader))
    root.add_resource(['file'], FileServer())
    asyncio.Task(aiocoap.Context.create_server_context(bind=(HOST_NAME, PORT_NUMBER), site = root))

    print(f'Server started on http://{HOST_NAME}:{PORT_NUMBER}')

    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
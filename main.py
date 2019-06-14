import requests
import json

if __name__ == '__main__':
    # url = 'http://httpbin.org/get'
    url = 'http://httpbin.org/post'
    #Este será el diccionario de parámetros que le vamos a meter a la url
    args = {'nombre':'juan', 'curso':'python', 'nivel':'intermedio'}
    #El argumento params sirve para enviarle los parámetros a la url
    # response = requests.get(url, params=args)
    response = requests.post(url, params=args)
    print(response)

    #Esto nos devolverá todo el html en el caso de que el estado del servidor sea 200 (OK)
    if response.status_code == 200:
        print(response.content)
        # content = response.content

        #por si queremos guardar todo lo que nos duelve el server en un fichero
        # file = open('google.html', 'wb')
        # file.write(content)
        # file.close()

        # respuesta_json = response.json() #Es el diccionario que nos devolverá el servidor
        # origin = respuesta_json['origin']
        # print(origin)

        #Esto nos devolveria el mismo resultado que lo anterior
        # respuesta_json = json.loads(response.text)
        # origin = respuesta_json['origin']
        # print(origin)

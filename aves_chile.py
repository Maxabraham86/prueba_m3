import requests
import json


def datos_aves():
    
    url = 'https://aves.ninjas.cl/api/birds'

    response = requests.get(url)
    if response.status_code ==200:
        return json.loads(response.text)

    else:
        print('Error al obtener los datos de las aves')
        return None
    
    
# html_completo = '''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Aves de Chile</title>
#     <style>
#         /* Estilos CSS opcionales */
#         .bird-card {
#             border: 1px solid #ccc;
#             border-radius: 5px;
#             padding: 10px;
#             margin: 10px;
#             display: inline-block;
#         }
#     </style>
# </head>
# <body>
#     <h1>Aves de Chile</h1>
#     <div id="bird-container">
#         <!-- Sección donde se agregarán las tarjetas de las aves -->
#     </div>
# </body>
# </html>
#'''
# def generate_bird_cards(birds_data):
#     cards= ''
#     for bird in birds_data:
#         cards += f'''
#         <div class="bird-card">
#             <h2>{bird['name']}</h2>
#             <img src="{bird['image']}" alt ="{bird['name']}">
#             <p><strong>Nombre en Español:</strong> {bird['spanishName']}</p>
#             <p><strong>Nombre en Ingles:</strong> {bird['englishName']}</p>
#         </div>
#         '''
#     return cards

photos= json.loads(photos.text)


card_col3=''
for photo in photos:
    card_col3 += f'''
                    <div class="card" style="width: 18rem;">
                        <img src="{bird['image']}" class="card-img-top" alt="...">
                        <div class="card-body">
                            <p><strong>Nombre en Español:</strong> {bird['spanishName']}</p>
                            <p><strong>Nombre en Ingles:</strong> {bird['englishName']}</p>
                        </div>
                    </div>
                    '''


print (card_col3)

def genera_html(content):
    with open('aves_de_chile.html','w') as f:
        f.write(html_completo)
        
def main():
    birds_data = datos_aves()
    if birds_data:
        bird_cards = generate_bird_cards(birds_data)
        with open('template.html', 'r') as f:
            template = f.read()
            final_html = template.replace
            genera_html(final_html)
        print("Sitio web generado correctamente como 'aves_de_chile.html'")
        
    else:
        print("No se pudo generar el sitio web debido a un error en la obtencion de los datos de las aves")
if __name__=="__main__":
    main()
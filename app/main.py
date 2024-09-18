from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

from animals import animals



class requestHandler(RequestHandler):
    def get(self):
        self.write(f"This route is working...")


class listRequestHandler(RequestHandler):
    def get(self):
        self.render("index.html")

class basicAnimalQueryRequestHandler(RequestHandler):
    def get (self):
        name = self.get_argument("name")

        for a in animals:
            if a['name'].lower() == name.lower():
                selected_animal = a
                break
            else:
                selected_animal = None

        if selected_animal:
            self.write(f"""
                <h1>Info about {selected_animal['name']}</h1>
                <p>Species: {selected_animal['species']}<p>
                <p>Habitat: {selected_animal['habitat']}<p>
                <p>Diet: {selected_animal['diet']}<p>
                <p>Avg Lifespan: {selected_animal['average_lifespan']}<p>
                <p>Status: {selected_animal['status']}<p>
            """)        
        else:
            self.write("Animal not found!")


class listAnimalsResourcesRequestHandler(RequestHandler):
    def get (self, resource):

        title = resource
        self.write(f"<h1>Animal {title}</h1>")

        list_animals = ""
        
        for a in animals:
            list_animals += f"""
                <li><strong>{a['name']}</strong>: {a[title]}</li>
            """
        
        self.write(f"""
            <ol>{list_animals}</ol>
        """)
            



if __name__ == "__main__":
    app = Application([
        (r"/", requestHandler),
        (r"/animals", listRequestHandler),
        (r"/animals/basic", basicAnimalQueryRequestHandler),
        (r"/animals/([A-Za-z]+)", listAnimalsResourcesRequestHandler)
        ])

    port = 7766
    app.listen(port)
    print(f"Listening on the port 7766")

    IOLoop.current().start()
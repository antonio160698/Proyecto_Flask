from flask import render_template_string, render_template, abort
class Example:
    def __init__(self):
        self.AUTHORS_INFO = {
            'poe':{
                'full_name':'Edgar Allan Poe',
                'nationality':'US',
                'notable_work':'The Raven',
                'born':'January 19 1809',
                'picture':'https://upload.wikimedia.org/wikipedia/commons/9/97/Edgar_Allan_Poe%2C_circa_1849%2C_restored%2C_squared_off.jpg'
            },
            'borges':{
                'full_name':'Jorge Luis Borges',
                'nationality':'Argentine',
                'notable_work':'The Aleph',
                'born':'August 24 1899',
                'picture':'https://upload.wikimedia.org/wikipedia/commons/c/cf/Jorge_Luis_Borges_1951%2C_by_Grete_Stern.jpg'
            }
            }
            

    def helloworld(self):
        html = """
        <html>
            <h1>Welcome to Library</h1>
            {authors_ul}
        </html>
        """
        authors = ["Edgar Alan Poe", "Jorge L. Borges", "Neil Gailman", "Mark Twain"]
        authors_list = "<ul>"
        authors_list += "\n".join([
            "<li>{author}</li>".format(author=author) for author in authors
        ])
        authors_list += "</ul>"
        return html.format(authors_ul=authors_list)
    
    def helloworld2(self):
        library_name = "Poe"
        html = """
        <html>
            <h1>Welcome to {{library}} Library</h1>
            <ul>
                {% for author in authors %}
                <li>{{author}}</li>
                {% endfor %}
            </ul>
        </html>
        """
        authors = ["Edgar Alan Poe", "Jorge L. Borges", "Neil Gailman", "Mark Twain"]
        rendered_html = render_template_string(html, library=library_name, authors=authors)
        return rendered_html
    
    def helloworld3(self):
        authors="Poe"
        return render_template('index.html', library=authors)

    def authors(self):
        return render_template('curso/authors.html')

    def author(self, author):
        if author not in self.AUTHORS_INFO:
            abort(404)
        return render_template('curso/author.html', author=self.AUTHORS_INFO[author])

    def abort_401(self):
        abort(400)
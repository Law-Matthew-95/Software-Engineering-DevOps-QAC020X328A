from website import create_app
from secure import SecureHeaders

secure_headers = SecureHeaders()
app = create_app()

@app.after_request
def after_request(response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response

if __name__ == '__main__':
    app.run(debug=True)
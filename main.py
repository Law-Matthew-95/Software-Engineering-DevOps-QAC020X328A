from website import create_app


app = create_app()

@app.after_request
def after_request(response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Content-Security-Policy'] = "default-src 'self'; style-src 'self' https://cdn.jsdelivr.net https://stackpath.bootstrapcdn.com; script-src 'self' https://code.jquery.com https://cdn.jsdelivr.net https://cdnjs.cloudflare.com https://maxcdn.bootstrapcdn.com; font-src 'self' https://cdn.jsdelivr.net https://stackpath.bootstrapcdn.com; img-src 'self'"
    response.headers['Referrer-Policy'] = 'no-referrer'
    response.headers['Permissions-Policy'] = "geolocation=(), microphone=(), camera=()"
    response.headers['strict-transport-security'] = 'max-age=31536000; includeSubDomains'
    return response


if __name__ == '__main__':
    app.run(debug=True)
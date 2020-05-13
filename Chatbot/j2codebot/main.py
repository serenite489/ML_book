from server import app


if __name__ == '__main__':
    print('Flask starting server...')
    app.run(
        host='127.0.0.1',
        port=3000,
        debug=True
    )

#Bash cmd to launch a ngrok tunnel
#ngrok http 300

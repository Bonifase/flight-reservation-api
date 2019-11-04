from flights import app
from multiprocessing import Process, Value
from helpers.send_email import send_email


if __name__ == '__main__':
    recording_on = Value('b', True)
    send_email = Process(target=send_email, args=(recording_on,))
    send_email.start()
    app.run(debug=True)
    send_email.join()
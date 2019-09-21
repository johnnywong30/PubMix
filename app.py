#####################
#
# PubMix
# Johnny Wong
#
#####################

import os

from flask import Flask, render_template, redirect, url_for, session, request, flash, get_flashed_messages

#============instantiate Flask object================
app = Flask(__name__)
app.secret_key = os.urandom(32)

#============Start of Routes========================

@app.route('/')
def index():
    return render_template('index.html')



#====================Run the App====================
if __name__ == '__main__':
    app.debug = True
    app.run()

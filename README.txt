In order to run this project, please be sure to have the pip package manager installed with the "virtualenv" program installed. Also be sure to have Python3. Lastly, use Homebrew to install "sox", which will be used to down sample our audio files. Create a virtual environment:

"virtualenv -p python3 venv"

And then activate the virtual environment:

"source venv/bin/activate"

Then install all of the dependencies needed:

"pip install -r requirements.txt"

This repo comes pre packaged with a model that is trained on the words "get, post, put, delete, patch." To run the program, launch the Flask web server:

"python FrontEnd/main.py"

Then navigate to "http://localhost:5000"

To train the model again:

"python speech_commands/train.py --data_url= --data_dir=dataset/ --wanted_words=get,post,put,delete"

Then save the model by running "freeze.py" in the speech_commands folder, being sure to plug in the same flags that you plugged in for the training file. You will have to tell the front end what checkpoint file to use, which is based on the number of epochs you trained your model on. 
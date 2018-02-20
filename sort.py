import os
import shutil
from guessit import guessit

MOVIEDB = os.environ['HOME'] + '/Videos'

VET = os.makedirs(os.environ['HOME'] + '/lft4hdj')


def find(folder):
    for newMovie in os.listdir(folder):
        movieInfo = guessit(newMovie)
        try:
            if 'container' in json.dumps(movieInfo):
                shutil.move(folder + '/' + newMovie, createDestinationDirectory(folder + '/' + movieInfo['title']))
                newMovie = movieInfo['title']
        except:

        if movieInfo['type'] == 'movie':
            moveDataAndDeleteFolder(folder + '/' + newMovie, createDestinationDirectory(MOVIEDB + '/Movies/' + movieInfo['title']))
        elif movieInfo['type'] == 'episode':
            moveDataAndDeleteFolder(folder + '/' + newMovie, createDestinationDirectory(MOVIEDB + '/Series/' + movieInfo['title'] + '/' + movieInfo['episode_title']))


def createDestinationDirectory(destinationDir):
    if not os.path.exists(destinationDir):
        os.makedirs(destinationDir)
    return destinationDir


def moveDataAndDeleteFolder(moviefolder, destinationDir):
    for fl in os.listdir(moviefolder):
        path = moviefolder + '/' + fl
        shutil.move(path, destinationDir)
    shutil.rmtree(moviefolder)

find(VET)
shutil.rmtree(os.environ['HOME'] + '/lft4hdj')

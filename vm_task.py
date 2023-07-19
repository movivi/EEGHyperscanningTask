#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on February 03, 2023, at 13:55
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard
import serial



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'vm_task'  # from the Builder filename that created this script
expInfo = {
    'participantA': f"{randint(0, 999999):06.0f}",
    'participantB': f"{randint(0, 999999):06.0f}",
    'group': '1',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s_%s' % (expInfo['participantA'], expInfo['participantB'], expInfo['group'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\BIZtech\\Desktop\\mo_VM\\vm_task.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], screen=2, 
    winType='pyglet', allowStencil=False,
    fullscr=True,
    #monitor='testMonitor', 
    color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False

winB = visual.Window(
    size=[1920, 1080], screen=1, 
    winType='pyglet', allowStencil=False,
    fullscr=True,
    #monitor='testMonitor', 
    color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
winB.mouseVisible = False

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / 60  # could not measure, so guess
else:
    frameDur = 1.0 / round(expInfo['frameRate'])
    
expInfo['frameRateB'] = winB.getActualFrameRate()
if expInfo['frameRateB'] != None:
    frameDurB = 1.0 / 60  # could not measure, so guess
else:
    frameDurB = 1.0 / round(expInfo['frameRateB'])
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Create serial object for Component "serialPort"
serialport = serial.Serial(
    port='COM1',
    baudrate=9600,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=None,
)
serialport.status = NOT_STARTED
if not serialport.is_open:
    serialport.open()

# --- Initialize components for Routine "instruction" ---
textA = visual.TextStim(win=win, name='textA',
    text='There are two parts to this memory experiment. \n\nThe first part called learning phase, you will be shown some images, please view them and pay attention. \nEach image will be shown inside a colored frame. If it’s a BLUE frame, then it means both you and the participant next to you is viewing the same image. \nIf it’s a YELLOW frame, then the image is only been shown to you and not to the other participant. \nSometimes no image may appear inside a WHITE frame. \n\nWhen an image appears, press 1 ASAP. When no image appears press 3 ASAP. \nBetween every trial you will see a fixation cross (+), no need to respond when you see fixation cross.\n\n\nIn the second part called testing phase, you will see some of the images you previously viewed as well as some new images. All images will be shown without the colored frame.\n\nOn each trial, you will be shown an image and you have to report ASAP whether it is an OLD or a NEW image.\n\nIf it’s an OLD image, press 9 ASAP. If it’s a NEW image, press 7 ASAP.\nBetween every trial you will see a fixation cross (+), no need to respond when you see a fixation cross.\n\nThere will be 6 blocks of this combination of learning and testing phases. Each block will last for about 3 minutes. There will be a 30-sec break after the 3rd block.\n\nPlease verbally paraphrase the instructions to the experimenter.\n\nNow, you will perform a series of practice trials.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
SPACE = keyboard.Keyboard()
textB = visual.TextStim(win=winB, name='textB',
    text='There are two parts to this memory experiment. \n\nThe first part called learning phase, you will be shown some images, please view them and pay attention. \nEach image will be shown inside a colored frame. If it’s a BLUE frame, then it means both you and the participant next to you is viewing the same image. \nIf it’s a YELLOW frame, then the image is only been shown to you and not to the other participant. \nSometimes no image may appear inside a WHITE frame. \n\nWhen an image appears, press 9 ASAP. When no image appears press 7 ASAP. \nBetween every trial you will see a fixation cross (+), no need to respond when you see fixation cross.\n\n\nIn the second part called testing phase, you will see some of the images you previously viewed as well as some new images. All images will be shown without the colored frame.\n\nOn each trial, you will be shown an image and you have to report ASAP whether it is an OLD or a NEW image.\n\nIf it’s an OLD image, press 1 ASAP. If it’s a NEW image, press 3 ASAP.\nBetween every trial you will see a fixation cross (+), no need to respond when you see a fixation cross.\n\nThere will be 6 blocks of this combination of learning and testing phases. Each block will last for about 3 minutes. There will be a 30-sec break after the 3rd block.\n\nPlease verbally paraphrase the instructions to the experimenter.\n\nNow, you will perform a series of practice trials.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "pracfix" ---
# Run 'Begin Experiment' code from codeprac
jitter = np.arange(1, 1.2, .10)
shuffle(jitter)
pracfixationA = visual.TextStim(win=win, name='pracfixationA',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
pracfixationB = visual.TextStim(win=winB, name='pracfixationB',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "pracimage" ---
p_port_pracimageA = parallel.ParallelPort(address='0x3FF8')
p_port_pracimageB = parallel.ParallelPort(address='0x3FF8')
pracborderA = visual.ImageStim(
    win=win,
    name='pracborderA', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.55, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
pracimageA = visual.ImageStim(
    win=win,
    name='pracimageA', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
prac_key_resp = keyboard.Keyboard()
pracborderB = visual.ImageStim(
    win=winB,
    name='pracborderB', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.55, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
pracimageB = visual.ImageStim(
    win=winB,
    name='pracimageB', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "pracinstruction" ---
pracTextA = visual.TextStim(win=win, name='pracTextA',
    text='Next is the testing phase.\n\nIf it’s an OLD image, press 9 ASAP. If it’s a NEW image, press 7 ASAP.\n\nPlease wait, the screen will automatically transition to testing phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
pracTextB = visual.TextStim(win=winB, name='pracTextB',
    text='Next is the testing phase.\n\nIf it’s an OLD image, press 1 ASAP. If it’s a NEW image, press 3 ASAP.\n\nPlease wait, the screen will automatically transition to testing phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "pracfixTT" ---
# Run 'Begin Experiment' code from codepracTT
jitter = np.arange(1, 1.2, .10)
shuffle(jitter)
pracfixationATT = visual.TextStim(win=win, name='pracfixationATT',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
pracfixationBTT = visual.TextStim(win=winB, name='pracfixationBTT',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "pracimageTT" ---
p_port_pracimageATT = parallel.ParallelPort(address='0x3FF8')
p_port_pracimageBTT = parallel.ParallelPort(address='0x3FF8')
pracimageATT = visual.ImageStim(
    win=win,
    name='pracimageATT', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
prac_key_respTT = keyboard.Keyboard()
pracimageBTT = visual.ImageStim(
    win=winB,
    name='pracimageBTT', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "instruction2" ---
textA_2 = visual.TextStim(win=win, name='textA_2',
    text="You have completed the practice trials.\n\nIf you have any doubts, please ask the experimenter now.\n\nPlease get ready for the main experiment. \n\nDuring the experiment, please control your eyeblinks (you can blink when you see the fixation cross +), head motion, and please don't apply pressure on your forehead. Please do not clench your teeth or breathe heavily. Please sit comfortably.\n\nRemember:\nDuring the learning phase, when an image appears press 1 ASAP. When no image appears press 3 ASAP. \n\nDuring the testing phase, when an OLD image appears press 9 ASAP. When a NEW image appears press 7 ASAP.",
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
SPACE_2 = keyboard.Keyboard()
textB_2 = visual.TextStim(win=winB, name='textB_2',
    text="You have completed the practice trials.\n\nIf you have any doubts, please ask the experimenter now.\n\nPlease get ready for the main experiment. \n\nDuring the experiment, please control your eyeblinks (you can blink when you see the fixation cross +), head motion, and please don't apply pressure on your forehead. Please do not clench your teeth or breathe heavily. Please sit comfortably.\n\nRemember:\nDuring the learning phase, when an image appears press 9 ASAP. When no image appears press 7 ASAP. \n\nDuring the testing phase, when an OLD image appears press 1 ASAP. When a NEW image appears press 3 ASAP.",
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "block1instruction" ---
block1TextA = visual.TextStim(win=win, name='block1TextA',
    text='Next is the 1st block of learning phase.\n\nIf an image appears, press 1 ASAP. If no image appears, press 3 ASAP.\n\nPlease wait, the screen will automatically transition to learning phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block1TextB = visual.TextStim(win=winB, name='block1TextB',
    text='Next is the 1st block of learning phase.\n\nIf an image appears, press 9 ASAP. If no image appears, press 7 ASAP.\n\nPlease wait, the screen will automatically transition to learning phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "block1fixation" ---
# Run 'Begin Experiment' code from code1
jitter = np.arange(1, 1.2, .10)
shuffle(jitter)
block1fixationA = visual.TextStim(win=win, name='block1fixationA',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block1fixationB = visual.TextStim(win=winB, name='block1fixationB',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "block1image" ---
p_port_block1imageA = parallel.ParallelPort(address='0x3FF8')
p_port_block1imageB = parallel.ParallelPort(address='0x3FF8')
block1borderA = visual.ImageStim(
    win=win,
    name='block1borderA', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.55, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
block1imageA = visual.ImageStim(
    win=win,
    name='block1imageA', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
block1key_resp = keyboard.Keyboard()
block1borderB = visual.ImageStim(
    win=winB,
    name='block1borderB', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.55, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
block1imageB = visual.ImageStim(
    win=winB,
    name='block1imageB', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "block1instructionTT" ---
block1TextATT = visual.TextStim(win=win, name='block1TextATT',
    text='Next is the testing phase.\n\nIf it’s an OLD image, press 9 ASAP. If it’s a NEW image, press 7 ASAP.\n\nPlease wait, the screen will automatically transition to testing phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block1TextBTT = visual.TextStim(win=winB, name='block1TextBTT',
    text='Next is the testing phase.\n\nIf it’s an OLD image, press 1 ASAP. If it’s a NEW image, press 3 ASAP.\n\nPlease wait, the screen will automatically transition to testing phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "block1fixationTT" ---
# Run 'Begin Experiment' code from code1TT
jitter = np.arange(1, 1.2, .10)
shuffle(jitter)
block1fixationATT = visual.TextStim(win=win, name='block1fixationATT',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block1fixationBTT = visual.TextStim(win=winB, name='block1fixationBTT',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "block1imageTT" ---
p_port_block1imageATT = parallel.ParallelPort(address='0x3FF8')
p_port_block1imageBTT = parallel.ParallelPort(address='0x3FF8')
block1imageATT = visual.ImageStim(
    win=win,
    name='block1imageATT', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
block1key_respTT = keyboard.Keyboard()
block1imageBTT = visual.ImageStim(
    win=winB,
    name='block1imageBTT', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "block2instruction" ---
block2TextA = visual.TextStim(win=win, name='block2TextA',
    text='Next is the 2nd block of learning phase.\n\nIf an image appears, press 1 ASAP. If no image appears, press 3 ASAP.\n\nPlease wait, the screen will automatically transition to learning phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block2TextB = visual.TextStim(win=winB, name='block2TextB',
    text='Next is the 2nd block of learning phase.\n\nIf an image appears, press 9 ASAP. If no image appears, press 7 ASAP.\n\nPlease wait, the screen will automatically transition to learning phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "block2fixation" ---
# Run 'Begin Experiment' code from code2
jitter = np.arange(1, 1.2, .10)
shuffle(jitter)
block2fixationA = visual.TextStim(win=win, name='block2fixationA',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block2fixationB = visual.TextStim(win=winB, name='block2fixationB',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "block2image" ---
p_port_block2imageA = parallel.ParallelPort(address='0x3FF8')
p_port_block2imageB = parallel.ParallelPort(address='0x3FF8')
block2borderA = visual.ImageStim(
    win=win,
    name='block2borderA', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.55, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
block2imageA = visual.ImageStim(
    win=win,
    name='block2imageA', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
block2key_resp = keyboard.Keyboard()
block2borderB = visual.ImageStim(
    win=winB,
    name='block2borderB', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.55, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
block2imageB = visual.ImageStim(
    win=winB,
    name='block2imageB', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "block2instructionTT" ---
block2TextATT = visual.TextStim(win=win, name='block2TextATT',
    text='Next is the testing phase.\n\nIf it’s an OLD image, press 9 ASAP. If it’s a NEW image, press 7 ASAP.\n\nPlease wait, the screen will automatically transition to testing phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block2TextBTT = visual.TextStim(win=winB, name='block2TextBTT',
    text='Next is the testing phase.\n\nIf it’s an OLD image, press 1 ASAP. If it’s a NEW image, press 3 ASAP.\n\nPlease wait, the screen will automatically transition to testing phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "block2fixationTT" ---
# Run 'Begin Experiment' code from code2TT
jitter = np.arange(1, 1.2, .10)
shuffle(jitter)
block2fixationATT = visual.TextStim(win=win, name='block2fixationATT',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block2fixationBTT = visual.TextStim(win=winB, name='block2fixationBTT',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "block2imageTT" ---
p_port_block2imageATT = parallel.ParallelPort(address='0x3FF8')
p_port_block2imageBTT = parallel.ParallelPort(address='0x3FF8')
block2imageATT = visual.ImageStim(
    win=win,
    name='block2imageATT', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
block2key_respTT = keyboard.Keyboard()
block2imageBTT = visual.ImageStim(
    win=winB,
    name='block2imageBTT', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "block3instruction" ---
block3TextA = visual.TextStim(win=win, name='block3TextA',
    text='Next is the 3rd block of learning phase.\n\nIf an image appears, press 1 ASAP. If no image appears, press 3 ASAP.\n\nPlease wait, the screen will automatically transition to learning phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block3TextB = visual.TextStim(win=winB, name='block3TextB',
    text='Next is the 3rd block of learning phase.\n\nIf an image appears, press 9 ASAP. If no image appears, press 7 ASAP.\n\nPlease wait, the screen will automatically transition to learning phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "block3fixation" ---
# Run 'Begin Experiment' code from code3
jitter = np.arange(1, 1.2, .10)
shuffle(jitter)
block3fixationA = visual.TextStim(win=win, name='block3fixationA',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block3fixationB = visual.TextStim(win=winB, name='block3fixationB',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "block3image" ---
p_port_block3imageA = parallel.ParallelPort(address='0x3FF8')
p_port_block3imageB = parallel.ParallelPort(address='0x3FF8')
block3borderA = visual.ImageStim(
    win=win,
    name='block3borderA', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.55, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
block3imageA = visual.ImageStim(
    win=win,
    name='block3imageA', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
block3key_resp = keyboard.Keyboard()
block3borderB = visual.ImageStim(
    win=winB,
    name='block3borderB', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.55, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
block3imageB = visual.ImageStim(
    win=winB,
    name='block3imageB', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "block3instructionTT" ---
block3TextATT = visual.TextStim(win=win, name='block3TextATT',
    text='Next is the testing phase.\n\nIf it’s an OLD image, press 9 ASAP. If it’s a NEW image, press 7 ASAP.\n\nPlease wait, the screen will automatically transition to testing phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block3TextBTT = visual.TextStim(win=winB, name='block3TextBTT',
    text='Next is the testing phase.\n\nIf it’s an OLD image, press 1 ASAP. If it’s a NEW image, press 3 ASAP.\n\nPlease wait, the screen will automatically transition to testing phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "block3fixationTT" ---
# Run 'Begin Experiment' code from code3TT
jitter = np.arange(1, 1.2, .10)
shuffle(jitter)
block3fixationATT = visual.TextStim(win=win, name='block3fixationATT',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block3fixationBTT = visual.TextStim(win=winB, name='block3fixationBTT',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "block3imageTT" ---
p_port_block3imageATT = parallel.ParallelPort(address='0x3FF8')
p_port_block3imageBTT = parallel.ParallelPort(address='0x3FF8')
block3imageATT = visual.ImageStim(
    win=win,
    name='block3imageATT', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
block3key_respTT = keyboard.Keyboard()
block3imageBTT = visual.ImageStim(
    win=winB,
    name='block3imageBTT', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "mainbreak" ---
breakTextA = visual.TextStim(win=win, name='breakTextA',
    text='Now you have a 30-sec break.\n\nAfter 30-sec, the experiment will automatically start so be ready.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
breakTextB = visual.TextStim(win=winB, name='breakTextB',
    text='Now you have a 30-sec break.\n\nAfter 30-sec, the experiment will automatically start so be ready.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "block4instruction" ---
block4TextA = visual.TextStim(win=win, name='block4TextA',
    text='Next is the 4th block of learning phase.\n\nIf an image appears, press 1 ASAP. If no image appears, press 3 ASAP.\n\nPlease wait, the screen will automatically transition to learning phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block4TextB = visual.TextStim(win=winB, name='block4TextB',
    text='Next is the 4th block of learning phase.\n\nIf an image appears, press 9 ASAP. If no image appears, press 7 ASAP.\n\nPlease wait, the screen will automatically transition to learning phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "block4fixation" ---
# Run 'Begin Experiment' code from code4
jitter = np.arange(1, 1.2, .10)
shuffle(jitter)
block4fixationA = visual.TextStim(win=win, name='block4fixationA',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block4fixationB = visual.TextStim(win=winB, name='block4fixationB',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "block4image" ---
p_port_block4imageA = parallel.ParallelPort(address='0x3FF8')
p_port_block4imageB = parallel.ParallelPort(address='0x3FF8')
block4borderA = visual.ImageStim(
    win=win,
    name='block4borderA', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.55, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
block4imageA = visual.ImageStim(
    win=win,
    name='block4imageA', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
block4key_resp = keyboard.Keyboard()
block4borderB = visual.ImageStim(
    win=winB,
    name='block4borderB', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.55, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
block4imageB = visual.ImageStim(
    win=winB,
    name='block4imageB', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "block4instructionTT" ---
block4TextATT = visual.TextStim(win=win, name='block4TextATT',
    text='Next is the testing phase.\n\nIf it’s an OLD image, press 9 ASAP. If it’s a NEW image, press 7 ASAP.\n\nPlease wait, the screen will automatically transition to testing phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block4TextBTT = visual.TextStim(win=winB, name='block4TextBTT',
    text='Next is the testing phase.\n\nIf it’s an OLD image, press 1 ASAP. If it’s a NEW image, press 3 ASAP.\n\nPlease wait, the screen will automatically transition to testing phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "block4fixationTT" ---
# Run 'Begin Experiment' code from code4TT
jitter = np.arange(1, 1.2, .10)
shuffle(jitter)
block4fixationATT = visual.TextStim(win=win, name='block4fixationATT',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block4fixationBTT = visual.TextStim(win=winB, name='block4fixationBTT',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "block4imageTT" ---
p_port_block4imageATT = parallel.ParallelPort(address='0x3FF8')
p_port_block4imageBTT = parallel.ParallelPort(address='0x3FF8')
block4imageATT = visual.ImageStim(
    win=win,
    name='block4imageATT', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
block4key_respTT = keyboard.Keyboard()
block4imageBTT = visual.ImageStim(
    win=winB,
    name='block4imageBTT', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "block5instruction" ---
block5TextA = visual.TextStim(win=win, name='block5TextA',
    text='Next is the 5th block of learning phase.\n\nIf an image appears, press 1 ASAP. If no image appears, press 3 ASAP.\n\nPlease wait, the screen will automatically transition to learning phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block5TextB = visual.TextStim(win=winB, name='block5TextB',
    text='Next is the 5th block of learning phase.\n\nIf an image appears, press 9 ASAP. If no image appears, press 7 ASAP.\n\nPlease wait, the screen will automatically transition to learning phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "block5fixation" ---
# Run 'Begin Experiment' code from code5
jitter = np.arange(1, 1.2, .10)
shuffle(jitter)
block5fixationA = visual.TextStim(win=win, name='block5fixationA',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block5fixationB = visual.TextStim(win=winB, name='block5fixationB',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "block5image" ---
p_port_block5imageA = parallel.ParallelPort(address='0x3FF8')
p_port_block5imageB = parallel.ParallelPort(address='0x3FF8')
block5borderA = visual.ImageStim(
    win=win,
    name='block5borderA', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.55, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
block5imageA = visual.ImageStim(
    win=win,
    name='block5imageA', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
block5key_resp = keyboard.Keyboard()
block5borderB = visual.ImageStim(
    win=winB,
    name='block5borderB', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.55, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
block5imageB = visual.ImageStim(
    win=winB,
    name='block5imageB', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "block5instructionTT" ---
block5TextATT = visual.TextStim(win=win, name='block5TextATT',
    text='Next is the testing phase.\n\nIf it’s an OLD image, press 9 ASAP. If it’s a NEW image, press 7 ASAP.\n\nPlease wait, the screen will automatically transition to testing phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block5TextBTT = visual.TextStim(win=winB, name='block5TextBTT',
    text='Next is the testing phase.\n\nIf it’s an OLD image, press 1 ASAP. If it’s a NEW image, press 3 ASAP.\n\nPlease wait, the screen will automatically transition to testing phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "block5fixationTT" ---
# Run 'Begin Experiment' code from code5TT
jitter = np.arange(1, 1.2, .10)
shuffle(jitter)
block5fixationATT = visual.TextStim(win=win, name='block5fixationATT',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block5fixationBTT = visual.TextStim(win=winB, name='block5fixationBTT',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "block5imageTT" ---
p_port_block5imageATT = parallel.ParallelPort(address='0x3FF8')
p_port_block5imageBTT = parallel.ParallelPort(address='0x3FF8')
block5imageATT = visual.ImageStim(
    win=win,
    name='block5imageATT', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
block5key_respTT = keyboard.Keyboard()
block5imageBTT = visual.ImageStim(
    win=winB,
    name='block5imageBTT', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "block6instruction" ---
block6TextA = visual.TextStim(win=win, name='block6TextA',
    text='Next is the 6th block of learning phase.\n\nIf an image appears, press 1 ASAP. If no image appears, press 3 ASAP.\n\nPlease wait, the screen will automatically transition to learning phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block6TextB = visual.TextStim(win=winB, name='block6TextB',
    text='Next is the 6th block of learning phase.\n\nIf an image appears, press 9 ASAP. If no image appears, press 7 ASAP.\n\nPlease wait, the screen will automatically transition to learning phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "block6fixation" ---
# Run 'Begin Experiment' code from code6
jitter = np.arange(1, 1.2, .10)
shuffle(jitter)
block6fixationA = visual.TextStim(win=win, name='block6fixationA',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block6fixationB = visual.TextStim(win=winB, name='block6fixationB',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "block6image" ---
p_port_block6imageA = parallel.ParallelPort(address='0x3FF8')
p_port_block6imageB = parallel.ParallelPort(address='0x3FF8')
block6borderA = visual.ImageStim(
    win=win,
    name='block6borderA', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.55, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
block6imageA = visual.ImageStim(
    win=win,
    name='block6imageA', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
block6key_resp = keyboard.Keyboard()
block6borderB = visual.ImageStim(
    win=winB,
    name='block6borderB', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.55, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
block6imageB = visual.ImageStim(
    win=winB,
    name='block6imageB', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "block6instructionTT" ---
block6TextATT = visual.TextStim(win=win, name='block6TextATT',
    text='Next is the testing phase.\n\nIf it’s an OLD image, press 9 ASAP. If it’s a NEW image, press 7 ASAP.\n\nPlease wait, the screen will automatically transition to testing phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block6TextBTT = visual.TextStim(win=winB, name='block6TextBTT',
    text='Next is the testing phase.\n\nIf it’s an OLD image, press 1 ASAP. If it’s a NEW image, press 3 ASAP.\n\nPlease wait, the screen will automatically transition to testing phase.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "block6fixationTT" ---
# Run 'Begin Experiment' code from code6TT
jitter = np.arange(1, 1.2, .10)
shuffle(jitter)
block6fixationATT = visual.TextStim(win=win, name='block6fixationATT',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block6fixationBTT = visual.TextStim(win=winB, name='block6fixationBTT',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "block6imageTT" ---
p_port_block6imageATT = parallel.ParallelPort(address='0x3FF8')
p_port_block6imageBTT = parallel.ParallelPort(address='0x3FF8')
block6imageATT = visual.ImageStim(
    win=win,
    name='block6imageATT', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
block6key_respTT = keyboard.Keyboard()
block6imageBTT = visual.ImageStim(
    win=winB,
    name='block6imageBTT', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "endmessage" ---
endTextA = visual.TextStim(win=win, name='endTextA',
    text='This is the end of the experiment.\n\nPlease remain seated and wait for the experimenter.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
endTextB = visual.TextStim(win=winB, name='endTextB',
    text='This is the end of the experiment.\n\nPlease remain seated and wait for the experimenter.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
SPACE_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instruction" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
SPACE.keys = []
SPACE.rt = []
_SPACE_allKeys = []
# keep track of which components have finished
instructionComponents = [textA, SPACE, textB]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "instruction" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textA* *textB* updates
    if textA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance and textB.status == NOT_STARTED:
        # keep track of start time/frame for later
        textA.frameNStart = frameN  # exact frame index
        textA.tStart = t  # local t and not account for scr refresh
        textA.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textA, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textA.started')
        textA.setAutoDraw(True)
        # keep track of start time/frame for later
        textB.frameNStart = frameNB  # exact frame index
        textB.tStart = tB  # local t and not account for scr refresh
        textB.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(textB, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'textB.started')
        textB.setAutoDraw(True)
    
    # *SPACE* updates
    waitOnFlip = False
    if SPACE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SPACE.frameNStart = frameN  # exact frame index
        SPACE.tStart = t  # local t and not account for scr refresh
        SPACE.tStartRefresh = tThisFlipGlobal  # on global time
        SPACE.frameNStart = frameNB  # exact frame index
        SPACE.tStart = tB  # local t and not account for scr refresh
        SPACE.tStartRefresh = tThisFlipGlobalB  # on global time
        win.timeOnFlip(SPACE, 'tStartRefresh')  # time at next scr refresh
        winB.timeOnFlip(SPACE, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'SPACE.started')
        thisExp.timestampOnFlip(winB, 'SPACEB.started')
        SPACE.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(SPACE.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(SPACE.clearEvents, eventType='keyboard')  # clear events on next screen flip
        winB.callOnFlip(SPACE.clock.reset)  # t=0 on next screen flip
        winB.callOnFlip(SPACE.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if SPACE.status == STARTED and not waitOnFlip:
        theseKeys = SPACE.getKeys(keyList=['space'], waitRelease=False)
        _SPACE_allKeys.extend(theseKeys)
        if len(_SPACE_allKeys):
            SPACE.keys = _SPACE_allKeys[-1].name  # just the last key pressed
            SPACE.rt = _SPACE_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "instruction" ---
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# check responses
if SPACE.keys in ['', [], None]:  # No response was made
    SPACE.keys = None
thisExp.addData('SPACE.keys',SPACE.keys)
if SPACE.keys != None:  # we had a response
    thisExp.addData('SPACE.rt', SPACE.rt)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('groupPB.xlsx'),
    seed=None, name='prac')
thisExp.addLoop(prac)  # add the loop to the experiment
thisPrac = prac.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac.rgb)
if thisPrac != None:
    for paramName in thisPrac:
        exec('{} = thisPrac[paramName]'.format(paramName))

for thisPrac in prac:
    currentLoop = prac
    # abbreviate parameter names if possible (e.g. rgb = thisPrac.rgb)
    if thisPrac != None:
        for paramName in thisPrac:
            exec('{} = thisPrac[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "pracfix" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from codeprac
    jitter = np.arange(1, 1.2, .10)
    shuffle(jitter)
    pracfixationA.setText('+')
    pracfixationB.setText('+')
    # keep track of which components have finished
    pracfixComponents = [pracfixationA, pracfixationB]
    for thisComponent in pracfixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "pracfix" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pracfixationA* *pracfixationB* updates
        if pracfixationA.status == NOT_STARTED and pracfixationB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracfixationA.frameNStart = frameN  # exact frame index
            pracfixationA.tStart = t  # local t and not account for scr refresh
            pracfixationA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracfixationA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracfixationA.started')
            pracfixationA.setAutoDraw(True)
            # keep track of start time/frame for later
            pracfixationB.frameNStart = frameNB  # exact frame index
            pracfixationB.tStart = tB  # local t and not account for scr refresh
            pracfixationB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(pracfixationB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'pracfixationB.started')
            pracfixationB.setAutoDraw(True)
        if pracfixationA.status == STARTED and pracfixationB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > pracfixationA.tStartRefresh + jitter[0]-frameTolerance) and (tThisFlipGlobalB > pracfixationB.tStartRefresh + jitter[0]-frameTolerance):
                # keep track of stop time/frame for later
                pracfixationA.tStop = t  # not accounting for scr refresh
                pracfixationA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracfixationA.stopped')
                pracfixationA.setAutoDraw(False)
                # keep track of stop time/frame for later
                pracfixationB.tStop = tB  # not accounting for scr refresh
                pracfixationB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'pracfixationB.stopped')
                pracfixationB.setAutoDraw(False)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracfixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "pracfix" ---
    for thisComponent in pracfixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    # the Routine "pracfix" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "pracimage" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    pracborderA.setImage(pracframeA)
    pracimageA.setImage(pracimagesA)
    prac_key_resp.keys = []
    prac_key_resp.rt = []
    _prac_key_resp_allKeys = []
    pracborderB.setImage(pracframeB)
    pracimageB.setImage(pracimagesB)
    # keep track of which components have finished
    pracimageComponents = [p_port_pracimageA,p_port_pracimageB, pracborderA, pracimageA, prac_key_resp, pracborderB, pracimageB]
    for thisComponent in pracimageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    # --- Run Routine "pracimage" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # update/draw components on each frame
        # *p_port_pracimageA* *p_port_pracimageB* updates
        if (p_port_pracimageA.status == NOT_STARTED and pracimageA.status == STARTED) and (p_port_pracimageB.status == NOT_STARTED and pracimageB.status == STARTED):
            # keep track of start time/frame for later
            p_port_pracimageA.frameNStart = frameN  # exact frame index
            p_port_pracimageA.tStart = t  # local t and not account for scr refresh
            p_port_pracimageA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_pracimageA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_port_pracimageA.started')
            p_port_pracimageA.status = STARTED
            win.callOnFlip(p_port_pracimageA.setData, int(pracCOA))
    
            # keep track of start time/frame for later
            #serialport.frameNStart = frameNB  # exact frame index
            #serialport.tStart = tB  # local t and not account for scr refresh
            #serialport.tStartRefresh = tThisFlipGlobalB  # on global time
            #winB.timeOnFlip(serialport, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(winB, 'serialport.started')
            #serialport.status = STARTED
            #winB.callOnFlip(serialport.write, bytes('pracCOB', 'utf8'))
            
            p_port_pracimageB.frameNStart = frameNB  # exact frame index
            p_port_pracimageB.tStart = tB  # local t and not account for scr refresh
            p_port_pracimageB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(p_port_pracimageB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'p_port_pracimageB.started')
            p_port_pracimageB.status = STARTED
            winB.callOnFlip(p_port_pracimageB.setData, int(pracCOB))
            
            
        if p_port_pracimageA.status == STARTED and p_port_pracimageB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > p_port_pracimageA.tStartRefresh + 0.1-frameTolerance) and (tThisFlipGlobalB > p_port_pracimageB.tStartRefresh + 0.1-frameTolerance):
                # keep track of stop time/frame for later
                p_port_pracimageA.tStop = t  # not accounting for scr refresh
                p_port_pracimageA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'p_port_pracimageA.stopped')
                p_port_pracimageA.status = FINISHED
                win.callOnFlip(p_port_pracimageA.setData, int(0))
                
                # keep track of stop time/frame for later
                #serialport.tStop = tB  # not accounting for scr refresh
                #serialport.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(winB, 'serialport.stopped')
                #serialport.status = FINISHED
                #winB.callOnFlip(serialport.write, bytes('0', 'utf8'))
                
                # keep track of stop time/frame for later
                p_port_pracimageB.tStop = tB  # not accounting for scr refresh
                p_port_pracimageB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'p_port_pracimageB.stopped')
                p_port_pracimageB.status = FINISHED
                winB.callOnFlip(p_port_pracimageB.setData, int(0))
        
        # *pracborderA* *pracborderB* updates
        if pracborderA.status == NOT_STARTED and pracborderB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracborderA.frameNStart = frameN  # exact frame index
            pracborderA.tStart = t  # local t and not account for scr refresh
            pracborderA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracborderA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracborderA.started')
            pracborderA.setAutoDraw(True)
            # keep track of start time/frame for later
            pracborderB.frameNStart = frameNB  # exact frame index
            pracborderB.tStart = tB  # local t and not account for scr refresh
            pracborderB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(pracborderB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'pracborderB.started')
            pracborderB.setAutoDraw(True)
        if pracborderA.status == STARTED and pracborderB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracborderA.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                pracborderA.tStop = t  # not accounting for scr refresh
                pracborderA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracborderA.stopped')
                pracborderA.setAutoDraw(False)
                # keep track of stop time/frame for later
                pracborderB.tStop = tB  # not accounting for scr refresh
                pracborderB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'pracborderB.stopped')
                pracborderB.setAutoDraw(False)
        
        # *pracimageA* *pracimageB* updates
        if pracimageA.status == NOT_STARTED and pracimageB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracimageA.frameNStart = frameN  # exact frame index
            pracimageA.tStart = t  # local t and not account for scr refresh
            pracimageA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracimageA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracimageA.started')
            pracimageA.setAutoDraw(True)
            # keep track of start time/frame for later
            pracimageB.frameNStart = frameNB  # exact frame index
            pracimageB.tStart = tB  # local t and not account for scr refresh
            pracimageB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(pracimageB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'pracimageB.started')
            pracimageB.setAutoDraw(True)
        if pracimageA.status == STARTED and pracimageB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracimageA.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                pracimageA.tStop = t  # not accounting for scr refresh
                pracimageA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracimageA.stopped')
                pracimageA.setAutoDraw(False)
                # keep track of stop time/frame for later
                pracimageB.tStop = tB  # not accounting for scr refresh
                pracimageB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'pracimageB.stopped')
                pracimageB.setAutoDraw(False)
        
        # *prac_key_resp* updates
        waitOnFlip = False
        if prac_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_key_resp.frameNStart = frameN  # exact frame index
            prac_key_resp.tStart = t  # local t and not account for scr refresh
            prac_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_key_resp, 'tStartRefresh')  # time at next scr refresh
            winB.timeOnFlip(prac_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_key_resp.started')
            thisExp.timestampOnFlip(winB, 'prac_key_respB.started')
            prac_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            winB.callOnFlip(prac_key_resp.clock.reset)  # t=0 on next screen flip
            winB.callOnFlip(prac_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_key_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                prac_key_resp.tStop = t  # not accounting for scr refresh
                prac_key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_key_resp.stopped')
                thisExp.timestampOnFlip(winB, 'prac_key_respB.stopped')
                prac_key_resp.status = FINISHED
        if prac_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = prac_key_resp.getKeys(keyList=['num_1','num_3','num_7','num_9'], waitRelease=False)
            _prac_key_resp_allKeys.extend(theseKeys)
            if len(_prac_key_resp_allKeys):
                prac_key_resp.keys = [key.name for key in _prac_key_resp_allKeys]  # storing all keys
                prac_key_resp.rt = [key.rt for key in _prac_key_resp_allKeys]
                # was this correct?
                if (prac_key_resp.keys == str(praccorrectkey)) or (prac_key_resp.keys == praccorrectkey):
                    prac_key_resp.corr = 1
                else:
                    prac_key_resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracimageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "pracimage" ---
    for thisComponent in pracimageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    if p_port_pracimageA.status == STARTED:
        win.callOnFlip(p_port_pracimageA.setData, int(0))
    if serialport.status == STARTED:
        winB.callOnFlip(serialport.write, bytes('0', 'utf8'))
    if p_port_pracimageB.status == STARTED:
        winB.callOnFlip(p_port_pracimageB.setData, int(0))
    # check responses
    if prac_key_resp.keys in ['', [], None]:  # No response was made
        prac_key_resp.keys = None
        # was no response the correct answer?!
        if str(praccorrectkey).lower() == 'none':
           prac_key_resp.corr = 1;  # correct non-response
        else:
           prac_key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for prac (TrialHandler)
    prac.addData('prac_key_resp.keys',prac_key_resp.keys)
    prac.addData('prac_key_resp.corr', prac_key_resp.corr)
    if prac_key_resp.keys != None:  # we had a response
        prac.addData('prac_key_resp.rt', prac_key_resp.rt)
    # the Routine "pracimage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'prac'


# --- Prepare to start Routine "pracinstruction" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
# keep track of which components have finished
pracinstructionComponents = [pracTextA, pracTextB]
for thisComponent in pracinstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "pracinstruction" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pracTextA* *pracTextB* updates
    if pracTextA.status == NOT_STARTED and pracTextB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracTextA.frameNStart = frameN  # exact frame index
        pracTextA.tStart = t  # local t and not account for scr refresh
        pracTextA.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracTextA, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pracTextA.started')
        pracTextA.setAutoDraw(True)
        # keep track of start time/frame for later
        pracTextB.frameNStart = frameNB  # exact frame index
        pracTextB.tStart = tB  # local t and not account for scr refresh
        pracTextB.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(pracTextB, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'pracTextB.started')
        pracTextB.setAutoDraw(True)
    if pracTextA.status == STARTED and pracTextB.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if (tThisFlipGlobal > pracTextA.tStartRefresh + 10-frameTolerance) and (tThisFlipGlobalB > pracTextB.tStartRefresh + 10-frameTolerance):
            # keep track of stop time/frame for later
            pracTextA.tStop = t  # not accounting for scr refresh
            pracTextA.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracTextA.stopped')
            pracTextA.setAutoDraw(False)
            # keep track of stop time/frame for later
            pracTextB.tStop = tB  # not accounting for scr refresh
            pracTextB.frameNStop = frameNB  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'pracTextB.stopped')
            pracTextB.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pracinstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "pracinstruction" ---
for thisComponent in pracinstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
pracTT = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('groupPBTT.xlsx'),
    seed=None, name='pracTT')
thisExp.addLoop(pracTT)  # add the loop to the experiment
thisPracTT = pracTT.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracTT.rgb)
if thisPracTT != None:
    for paramName in thisPracTT:
        exec('{} = thisPracTT[paramName]'.format(paramName))

for thisPracTT in pracTT:
    currentLoop = pracTT
    # abbreviate parameter names if possible (e.g. rgb = thisPracTT.rgb)
    if thisPracTT != None:
        for paramName in thisPracTT:
            exec('{} = thisPracTT[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "pracfixTT" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from codepracTT
    jitter = np.arange(1, 1.2, .10)
    shuffle(jitter)
    pracfixationATT.setText('+')
    pracfixationBTT.setText('+')
    # keep track of which components have finished
    pracfixTTComponents = [pracfixationATT, pracfixationBTT]
    for thisComponent in pracfixTTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "pracfixTT" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pracfixationATT* *pracfixationBTT* updates
        if pracfixationATT.status == NOT_STARTED and pracfixationBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracfixationATT.frameNStart = frameN  # exact frame index
            pracfixationATT.tStart = t  # local t and not account for scr refresh
            pracfixationATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracfixationATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracfixationATT.started')
            pracfixationATT.setAutoDraw(True)
            # keep track of start time/frame for later
            pracfixationBTT.frameNStart = frameNB  # exact frame index
            pracfixationBTT.tStart = tB  # local t and not account for scr refresh
            pracfixationBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(pracfixationBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'pracfixationBTT.started')
            pracfixationBTT.setAutoDraw(True)
        if pracfixationATT.status == STARTED and pracfixationBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > pracfixationATT.tStartRefresh + jitter[0]-frameTolerance) and (tThisFlipGlobalB > pracfixationBTT.tStartRefresh + jitter[0]-frameTolerance):
                # keep track of stop time/frame for later
                pracfixationATT.tStop = t  # not accounting for scr refresh
                pracfixationATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracfixationATT.stopped')
                pracfixationATT.setAutoDraw(False)
                # keep track of stop time/frame for later
                pracfixationBTT.tStop = tB  # not accounting for scr refresh
                pracfixationBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'pracfixationBTT.stopped')
                pracfixationBTT.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracfixTTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "pracfixTT" ---
    for thisComponent in pracfixTTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    # the Routine "pracfixTT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "pracimageTT" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    pracimageATT.setImage(pracimagesATT)
    prac_key_respTT.keys = []
    prac_key_respTT.rt = []
    _prac_key_respTT_allKeys = []
    pracimageBTT.setImage(pracimagesBTT)
    # keep track of which components have finished
    pracimageTTComponents = [p_port_pracimageATT, p_port_pracimageBTT, pracimageATT, prac_key_respTT, pracimageBTT]
    for thisComponent in pracimageTTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "pracimageTT" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # update/draw components on each frame
        # *p_port_pracimageA* *p_port_pracimageB* updates
        if (p_port_pracimageATT.status == NOT_STARTED and pracimageATT.status == STARTED) and (p_port_pracimageBTT.status == NOT_STARTED and pracimageBTT.status == STARTED):
            # keep track of start time/frame for later
            p_port_pracimageATT.frameNStart = frameN  # exact frame index
            p_port_pracimageATT.tStart = t  # local t and not account for scr refresh
            p_port_pracimageATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_pracimageATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_port_pracimageATT.started')
            p_port_pracimageATT.status = STARTED
            win.callOnFlip(p_port_pracimageATT.setData, int(pracCOATT))
    
            # keep track of start time/frame for later
            #serialport.frameNStart = frameNB  # exact frame index
            #serialport.tStart = tB  # local t and not account for scr refresh
            #serialport.tStartRefresh = tThisFlipGlobalB  # on global time
            #winB.timeOnFlip(serialport, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(winB, 'serialport.started')
            #serialport.status = STARTED
            #winB.callOnFlip(serialport.write, bytes('pracCOB', 'utf8'))
            
            p_port_pracimageBTT.frameNStart = frameNB  # exact frame index
            p_port_pracimageBTT.tStart = tB  # local t and not account for scr refresh
            p_port_pracimageBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(p_port_pracimageBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'p_port_pracimageBTT.started')
            p_port_pracimageBTT.status = STARTED
            winB.callOnFlip(p_port_pracimageBTT.setData, int(pracCOBTT))
            
            
        if p_port_pracimageATT.status == STARTED and p_port_pracimageBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > p_port_pracimageATT.tStartRefresh + 0.1-frameTolerance) and (tThisFlipGlobalB > p_port_pracimageBTT.tStartRefresh + 0.1-frameTolerance):
                # keep track of stop time/frame for later
                p_port_pracimageATT.tStop = t  # not accounting for scr refresh
                p_port_pracimageATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'p_port_pracimageATT.stopped')
                p_port_pracimageATT.status = FINISHED
                win.callOnFlip(p_port_pracimageATT.setData, int(0))
                
                # keep track of stop time/frame for later
                #serialport.tStop = tB  # not accounting for scr refresh
                #serialport.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(winB, 'serialport.stopped')
                #serialport.status = FINISHED
                #winB.callOnFlip(serialport.write, bytes('0', 'utf8'))
                
                # keep track of stop time/frame for later
                p_port_pracimageBTT.tStop = tB  # not accounting for scr refresh
                p_port_pracimageBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'p_port_pracimageBTT.stopped')
                p_port_pracimageBTT.status = FINISHED
                winB.callOnFlip(p_port_pracimageBTT.setData, int(0))
        
        # *pracimageATT* *pracimageBTT* updates
        if pracimageATT.status == NOT_STARTED and pracimageBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracimageATT.frameNStart = frameN  # exact frame index
            pracimageATT.tStart = t  # local t and not account for scr refresh
            pracimageATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracimageATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracimageATT.started')
            pracimageATT.setAutoDraw(True)
            # keep track of start time/frame for later
            pracimageBTT.frameNStart = frameNB  # exact frame index
            pracimageBTT.tStart = tB  # local t and not account for scr refresh
            pracimageBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(pracimageBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'pracimageBTT.started')
            pracimageBTT.setAutoDraw(True)
        if pracimageATT.status == STARTED and pracimageBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > pracimageATT.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > pracimageBTT.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                pracimageATT.tStop = t  # not accounting for scr refresh
                pracimageATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracimageATT.stopped')
                pracimageATT.setAutoDraw(False)
                # keep track of stop time/frame for later
                pracimageBTT.tStop = tB  # not accounting for scr refresh
                pracimageBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'pracimageBTT.stopped')
                pracimageBTT.setAutoDraw(False)
        
        # *prac_key_respTT* updates
        waitOnFlip = False
        if prac_key_respTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_key_respTT.frameNStart = frameN  # exact frame index
            prac_key_respTT.tStart = t  # local t and not account for scr refresh
            prac_key_respTT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_key_respTT, 'tStartRefresh')  # time at next scr refresh
            winB.timeOnFlip(prac_key_respTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_key_respTT.started')
            thisExp.timestampOnFlip(winB, 'prac_key_respTTB.started')
            prac_key_respTT.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_key_respTT.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_key_respTT.clearEvents, eventType='keyboard')  # clear events on next screen flip
            winB.callOnFlip(prac_key_respTT.clock.reset)  # t=0 on next screen flip
            winB.callOnFlip(prac_key_respTT.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_key_respTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_key_respTT.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                prac_key_respTT.tStop = t  # not accounting for scr refresh
                prac_key_respTT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_key_respTT.stopped')
                thisExp.timestampOnFlip(winB, 'prac_key_respTTB.stopped')
                prac_key_respTT.status = FINISHED
        if prac_key_respTT.status == STARTED and not waitOnFlip:
            theseKeys = prac_key_respTT.getKeys(keyList=['num_1','num_3','num_7','num_9'], waitRelease=False)
            _prac_key_respTT_allKeys.extend(theseKeys)
            if len(_prac_key_respTT_allKeys):
                prac_key_respTT.keys = [key.name for key in _prac_key_resp_allKeys]  # storing all keys
                prac_key_respTT.rt = [key.rt for key in _prac_key_resp_allKeys]
                # was this correct?
                if (prac_key_respTT.keys == str(praccorrectkeyTT)) or (prac_key_respTT.keys == praccorrectkeyTT):
                    prac_key_respTT.corr = 1
                else:
                    prac_key_respTT.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracimageTTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "pracimageTT" ---
    for thisComponent in pracimageTTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    if p_port_pracimageATT.status == STARTED:
        win.callOnFlip(p_port_pracimageATT.setData, int(0))
    if p_port_pracimageBTT.status == STARTED:
        winB.callOnFlip(p_port_pracimageBTT.setData, int(0))
    # check responses
    if prac_key_respTT.keys in ['', [], None]:  # No response was made
        prac_key_respTT.keys = None
        # was no response the correct answer?!
        if str(praccorrectkeyTT).lower() == 'none':
           prac_key_respTT.corr = 1;  # correct non-response
        else:
           prac_key_respTT.corr = 0;  # failed to respond (incorrectly)
    # store data for pracTT (TrialHandler)
    pracTT.addData('prac_key_respTT.keys',prac_key_respTT.keys)
    pracTT.addData('prac_key_respTT.corr', prac_key_respTT.corr)
    if prac_key_respTT.keys != None:  # we had a response
        pracTT.addData('prac_key_respTT.rt', prac_key_respTT.rt)
    # the Routine "pracimageTT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'pracTT'


# --- Prepare to start Routine "instruction2" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
SPACE_2.keys = []
SPACE_2.rt = []
_SPACE_2_allKeys = []
# keep track of which components have finished
instruction2Components = [textA_2, SPACE_2, textB_2]
for thisComponent in instruction2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "instruction2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textA_2* *textB_2* updates
    if textA_2.status == NOT_STARTED and textB_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textA_2.frameNStart = frameN  # exact frame index
        textA_2.tStart = t  # local t and not account for scr refresh
        textA_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textA_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textA_2.started')
        textA_2.setAutoDraw(True)
        # keep track of start time/frame for later
        textB_2.frameNStart = frameNB  # exact frame index
        textB_2.tStart = tB  # local t and not account for scr refresh
        textB_2.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(textB_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'textB_2.started')
        textB_2.setAutoDraw(True)
    
    # *SPACE_2* updates
    waitOnFlip = False
    if SPACE_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SPACE_2.frameNStart = frameN  # exact frame index
        SPACE_2.tStart = t  # local t and not account for scr refresh
        SPACE_2.tStartRefresh = tThisFlipGlobal  # on global time
        SPACE_2.frameNStart = frameNB  # exact frame index
        SPACE_2.tStart = tB  # local t and not account for scr refresh
        SPACE_2.tStartRefresh = tThisFlipGlobalB  # on global time
        win.timeOnFlip(SPACE_2, 'tStartRefresh')  # time at next scr refresh
        winB.timeOnFlip(SPACE_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'SPACE_2.started')
        thisExp.timestampOnFlip(winB, 'SPACE_2B.started')
        SPACE_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(SPACE_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(SPACE_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        winB.callOnFlip(SPACE_2.clock.reset)  # t=0 on next screen flip
        winB.callOnFlip(SPACE_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if SPACE_2.status == STARTED and not waitOnFlip:
        theseKeys = SPACE_2.getKeys(keyList=['space'], waitRelease=False)
        _SPACE_2_allKeys.extend(theseKeys)
        if len(_SPACE_2_allKeys):
            SPACE_2.keys = _SPACE_2_allKeys[-1].name  # just the last key pressed
            SPACE_2.rt = _SPACE_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "instruction2" ---
for thisComponent in instruction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# check responses
if SPACE_2.keys in ['', [], None]:  # No response was made
    SPACE_2.keys = None
thisExp.addData('SPACE_2.keys',SPACE_2.keys)
if SPACE_2.keys != None:  # we had a response
    thisExp.addData('SPACE_2.rt', SPACE_2.rt)
thisExp.nextEntry()
# the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "block1instruction" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
# keep track of which components have finished
block1instructionComponents = [block1TextA, block1TextB]
for thisComponent in block1instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "block1instruction" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block1TextA* *block1TextB* updates
    if block1TextA.status == NOT_STARTED and block1TextB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block1TextA.frameNStart = frameN  # exact frame index
        block1TextA.tStart = t  # local t and not account for scr refresh
        block1TextA.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block1TextA, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'block1TextA.started')
        block1TextA.setAutoDraw(True)
        # keep track of start time/frame for later
        block1TextB.frameNStart = frameNB  # exact frame index
        block1TextB.tStart = tB  # local t and not account for scr refresh
        block1TextB.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(block1TextB, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'block1TextB.started')
        block1TextB.setAutoDraw(True)
        
    if block1TextA.status == STARTED and block1TextB.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if (tThisFlipGlobal > block1TextA.tStartRefresh + 10-frameTolerance) and (tThisFlipGlobalB > block1TextB.tStartRefresh + 10-frameTolerance):
            # keep track of stop time/frame for later
            block1TextA.tStop = t  # not accounting for scr refresh
            block1TextA.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block1TextA.stopped')
            block1TextA.setAutoDraw(False)
             # keep track of stop time/frame for later
            block1TextB.tStop = tB  # not accounting for scr refresh
            block1TextB.frameNStop = frameNB  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block1TextB.stopped')
            block1TextB.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block1instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "block1instruction" ---
for thisComponent in block1instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
block1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('group1_b1.xlsx'),
    seed=None, name='block1')
thisExp.addLoop(block1)  # add the loop to the experiment
thisBlock1 = block1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
if thisBlock1 != None:
    for paramName in thisBlock1:
        exec('{} = thisBlock1[paramName]'.format(paramName))

for thisBlock1 in block1:
    currentLoop = block1
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
    if thisBlock1 != None:
        for paramName in thisBlock1:
            exec('{} = thisBlock1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block1fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code1
    jitter = np.arange(1, 1.2, .10)
    shuffle(jitter)
    block1fixationA.setText('+')
    block1fixationB.setText('+')
    # keep track of which components have finished
    block1fixationComponents = [block1fixationA, block1fixationB]
    for thisComponent in block1fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block1fixation" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block1fixationA* *block1fixationB* updates
        if block1fixationA.status == NOT_STARTED and block1fixationB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block1fixationA.frameNStart = frameN  # exact frame index
            block1fixationA.tStart = t  # local t and not account for scr refresh
            block1fixationA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block1fixationA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block1fixationA.started')
            block1fixationA.setAutoDraw(True)
            # keep track of start time/frame for later
            block1fixationB.frameNStart = frameNB  # exact frame index
            block1fixationB.tStart = tB  # local t and not account for scr refresh
            block1fixationB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block1fixationB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block1fixationB.started')
            block1fixationB.setAutoDraw(True)
        if block1fixationA.status == STARTED and block1fixationB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block1fixationA.tStartRefresh + jitter[0]-frameTolerance) and (tThisFlipGlobalB > block1fixationB.tStartRefresh + jitter[0]-frameTolerance):
                # keep track of stop time/frame for later
                block1fixationA.tStop = t  # not accounting for scr refresh
                block1fixationA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block1fixationA.stopped')
                block1fixationA.setAutoDraw(False)
                # keep track of stop time/frame for later
                block1fixationB.tStop = tB  # not accounting for scr refresh
                block1fixationB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block1fixationB.stopped')
                block1fixationB.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block1fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block1fixation" ---
    for thisComponent in block1fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    # the Routine "block1fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block1image" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    block1borderA.setImage(frameA1)
    block1imageA.setImage(imagesA1)
    block1key_resp.keys = []
    block1key_resp.rt = []
    _block1key_resp_allKeys = []
    block1borderB.setImage(frameB1)
    block1imageB.setImage(imagesB1)
    # keep track of which components have finished
    block1imageComponents = [p_port_block1imageA, p_port_block1imageB, block1borderA, block1imageA, block1key_resp, block1borderB, block1imageB]
    for thisComponent in block1imageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block1image" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # update/draw components on each frame
        # *p_port_block1imageA* *p_port_block1imageB* updates
        if (p_port_block1imageA.status == NOT_STARTED and block1imageA.status == STARTED) and (p_port_block1imageB.status == NOT_STARTED and block1imageB.status == STARTED):
            # keep track of start time/frame for later
            p_port_block1imageA.frameNStart = frameN  # exact frame index
            p_port_block1imageA.tStart = t  # local t and not account for scr refresh
            p_port_block1imageA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_block1imageA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_port_block1imageA.started')
            p_port_block1imageA.status = STARTED
            win.callOnFlip(p_port_block1imageA.setData, int(COA1))
    
            # keep track of start time/frame for later
            #serialport.frameNStart = frameNB  # exact frame index
            #serialport.tStart = tB  # local t and not account for scr refresh
            #serialport.tStartRefresh = tThisFlipGlobalB  # on global time
            #winB.timeOnFlip(serialport, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(winB, 'serialport.started')
            #serialport.status = STARTED
            #winB.callOnFlip(serialport.write, bytes('pracCOB', 'utf8'))
            
            p_port_block1imageB.frameNStart = frameNB  # exact frame index
            p_port_block1imageB.tStart = tB  # local t and not account for scr refresh
            p_port_block1imageB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(p_port_block1imageB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'p_port_block1imageB.started')
            p_port_block1imageB.status = STARTED
            winB.callOnFlip(p_port_block1imageB.setData, int(COB1))
            
            
        if p_port_block1imageA.status == STARTED and p_port_block1imageB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > p_port_block1imageA.tStartRefresh + 0.1-frameTolerance) and (tThisFlipGlobalB > p_port_block1imageB.tStartRefresh + 0.1-frameTolerance):
                # keep track of stop time/frame for later
                p_port_block1imageA.tStop = t  # not accounting for scr refresh
                p_port_block1imageA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'p_port_block1imageA.stopped')
                p_port_block1imageA.status = FINISHED
                win.callOnFlip(p_port_block1imageA.setData, int(0))
                
                # keep track of stop time/frame for later
                #serialport.tStop = tB  # not accounting for scr refresh
                #serialport.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(winB, 'serialport.stopped')
                #serialport.status = FINISHED
                #winB.callOnFlip(serialport.write, bytes('0', 'utf8'))
                
                # keep track of stop time/frame for later
                p_port_block1imageB.tStop = tB  # not accounting for scr refresh
                p_port_block1imageB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'p_port_block1imageB.stopped')
                p_port_block1imageB.status = FINISHED
                winB.callOnFlip(p_port_block1imageB.setData, int(0))
        
        # *block1borderA* *block1borderB* updates
        if block1borderA.status == NOT_STARTED and block1borderB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block1borderA.frameNStart = frameN  # exact frame index
            block1borderA.tStart = t  # local t and not account for scr refresh
            block1borderA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block1borderA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block1borderA.started')
            block1borderA.setAutoDraw(True)
            # keep track of start time/frame for later
            block1borderB.frameNStart = frameNB  # exact frame index
            block1borderB.tStart = tB  # local t and not account for scr refresh
            block1borderB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block1borderB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block1borderB.started')
            block1borderB.setAutoDraw(True)
            
        if block1borderA.status == STARTED and block1borderB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block1borderA.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block1borderB.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block1borderA.tStop = t  # not accounting for scr refresh
                block1borderA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block1borderA.stopped')
                block1borderA.setAutoDraw(False)
                # keep track of stop time/frame for later
                block1borderB.tStop = tB  # not accounting for scr refresh
                block1borderB.frameNStop = frameNB # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block1borderB.stopped')
                block1borderB.setAutoDraw(False)
        
        # *block1imageA* *block1imageB* updates
        if block1imageA.status == NOT_STARTED and block1imageB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block1imageA.frameNStart = frameN  # exact frame index
            block1imageA.tStart = t  # local t and not account for scr refresh
            block1imageA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block1imageA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block1imageA.started')
            block1imageA.setAutoDraw(True)
            # keep track of start time/frame for later
            block1imageB.frameNStart = frameNB  # exact frame index
            block1imageB.tStart = tB  # local t and not account for scr refresh
            block1imageB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block1imageB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block1imageB.started')
            block1imageB.setAutoDraw(True)
            
        if block1imageA.status == STARTED and block1imageB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block1imageA.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block1imageB.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block1imageA.tStop = t  # not accounting for scr refresh
                block1imageA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block1imageA.stopped')
                block1imageA.setAutoDraw(False)
                 # keep track of stop time/frame for later
                block1imageB.tStop = tB  # not accounting for scr refresh
                block1imageB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block1imageB.stopped')
                block1imageB.setAutoDraw(False)
        
        # *block1key_resp* updates
        waitOnFlip = False
        if block1key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block1key_resp.frameNStart = frameN  # exact frame index
            block1key_resp.tStart = t  # local t and not account for scr refresh
            block1key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block1key_resp, 'tStartRefresh')  # time at next scr refresh
            winB.timeOnFlip(block1key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block1key_resp.started')
            thisExp.timestampOnFlip(winB, 'block1key_respB.started')
            block1key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block1key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block1key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            winB.callOnFlip(block1key_resp.clock.reset)  # t=0 on next screen flip
            winB.callOnFlip(block1key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block1key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block1key_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                block1key_resp.tStop = t  # not accounting for scr refresh
                block1key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block1key_resp.stopped')
                thisExp.timestampOnFlip(winB, 'block1key_respB.stopped')
                block1key_resp.status = FINISHED
        if block1key_resp.status == STARTED and not waitOnFlip:
            theseKeys = block1key_resp.getKeys(keyList=['num_1','num_3','num_7','num_9'], waitRelease=False)
            _block1key_resp_allKeys.extend(theseKeys)
            if len(_block1key_resp_allKeys):
                block1key_resp.keys = [key.name for key in _block1key_resp_allKeys]  # storing all keys
                block1key_resp.rt = [key.rt for key in _block1key_resp_allKeys]
                # was this correct?
                if (block1key_resp.keys == str(correctkey1)) or (prac_key_resp.keys == correctkey1):
                    block1key_resp.corr = 1
                else:
                    block1key_resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block1imageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block1image" ---
    for thisComponent in block1imageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    if p_port_block1imageA.status == STARTED:
        win.callOnFlip(p_port_block1imageA.setData, int(0))
    if p_port_block1imageB.status == STARTED:
        winB.callOnFlip(p_port_block1imageB.setData, int(0))
    # check responses
    if block1key_resp.keys in ['', [], None]:  # No response was made
        block1key_resp.keys = None
        # was no response the correct answer?!
        if str(correctkey1).lower() == 'none':
           block1key_resp.corr = 1;  # correct non-response
        else:
           block1key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for block1 (TrialHandler)
    block1.addData('block1key_resp.keys',block1key_resp.keys)
    block1.addData('block1key_resp.corr', block1key_resp.corr)
    if block1key_resp.keys != None:  # we had a response
        block1.addData('block1key_resp.rt', block1key_resp.rt)
    # the Routine "block1image" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block1'


# --- Prepare to start Routine "block1instructionTT" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
# keep track of which components have finished
block1instructionTTComponents = [block1TextATT, block1TextBTT]
for thisComponent in block1instructionTTComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "block1instructionTT" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block1TextATT* *block1TextBTT* updates
    if block1TextATT.status == NOT_STARTED and block1TextBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block1TextATT.frameNStart = frameN  # exact frame index
        block1TextATT.tStart = t  # local t and not account for scr refresh
        block1TextATT.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block1TextATT, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'block1TextATT.started')
        block1TextATT.setAutoDraw(True)
        # keep track of start time/frame for later
        block1TextBTT.frameNStart = frameNB  # exact frame index
        block1TextBTT.tStart = tB  # local t and not account for scr refresh
        block1TextBTT.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(block1TextBTT, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'block1TextBTT.started')
        block1TextBTT.setAutoDraw(True)
        
    if block1TextATT.status == STARTED and block1TextBTT.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if (tThisFlipGlobal > block1TextATT.tStartRefresh + 10-frameTolerance) and (tThisFlipGlobalB > block1TextBTT.tStartRefresh + 10-frameTolerance):
            # keep track of stop time/frame for later
            block1TextATT.tStop = t  # not accounting for scr refresh
            block1TextATT.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block1TextATT.stopped')
            block1TextATT.setAutoDraw(False)
            # keep track of stop time/frame for later
            block1TextBTT.tStop = tB  # not accounting for scr refresh
            block1TextBTT.frameNStop = frameNB  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block1TextBTT.stopped')
            block1TextBTT.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block1instructionTTComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "block1instructionTT" ---
for thisComponent in block1instructionTTComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
block1TT = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('group1_b1TT.xlsx'),
    seed=None, name='block1TT')
thisExp.addLoop(block1TT)  # add the loop to the experiment
thisBlock1TT = block1TT.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock1TT.rgb)
if thisBlock1TT != None:
    for paramName in thisBlock1TT:
        exec('{} = thisBlock1TT[paramName]'.format(paramName))

for thisBlock1TT in block1TT:
    currentLoop = block1TT
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1TT.rgb)
    if thisBlock1TT != None:
        for paramName in thisBlock1TT:
            exec('{} = thisBlock1TT[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block1fixationTT" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code1TT
    jitter = np.arange(1, 1.2, .10)
    shuffle(jitter)
    block1fixationATT.setText('+')
    block1fixationBTT.setText('+')
    # keep track of which components have finished
    block1fixationTTComponents = [block1fixationATT, block1fixationBTT]
    for thisComponent in block1fixationTTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block1fixationTT" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block1fixationATT* *block1fixationBTT* updates
        if block1fixationATT.status == NOT_STARTED and block1fixationBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block1fixationATT.frameNStart = frameN  # exact frame index
            block1fixationATT.tStart = t  # local t and not account for scr refresh
            block1fixationATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block1fixationATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block1fixationATT.started')
            block1fixationATT.setAutoDraw(True)
            # keep track of start time/frame for later
            block1fixationBTT.frameNStart = frameNB  # exact frame index
            block1fixationBTT.tStart = tB  # local t and not account for scr refresh
            block1fixationBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block1fixationBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block1fixationBTT.started')
            block1fixationBTT.setAutoDraw(True)
        
        if block1fixationATT.status == STARTED and block1fixationBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block1fixationATT.tStartRefresh + jitter[0]-frameTolerance) and (tThisFlipGlobalB > block1fixationBTT.tStartRefresh + jitter[0]-frameTolerance):
                # keep track of stop time/frame for later
                block1fixationATT.tStop = t  # not accounting for scr refresh
                block1fixationATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block1fixationATT.stopped')
                block1fixationATT.setAutoDraw(False)
                # keep track of stop time/frame for later
                block1fixationBTT.tStop = tB  # not accounting for scr refresh
                block1fixationBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block1fixationBTT.stopped')
                block1fixationBTT.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block1fixationTTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block1fixationTT" ---
    for thisComponent in block1fixationTTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    # the Routine "block1fixationTT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block1imageTT" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    block1imageATT.setImage(imagesA1TT)
    block1key_respTT.keys = []
    block1key_respTT.rt = []
    _block1key_respTT_allKeys = []
    block1imageBTT.setImage(imagesB1TT)
    # keep track of which components have finished
    block1imageTTComponents = [p_port_block1imageATT, p_port_block1imageBTT, block1imageATT, block1key_respTT, block1imageBTT]
    for thisComponent in block1imageTTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block1imageTT" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_port_block1imageA* *p_port_block1imageB* updates
        if (p_port_block1imageATT.status == NOT_STARTED and block1imageATT.status == STARTED) and (p_port_block1imageBTT.status == NOT_STARTED and block1imageBTT.status == STARTED):
            # keep track of start time/frame for later
            p_port_block1imageATT.frameNStart = frameN  # exact frame index
            p_port_block1imageATT.tStart = t  # local t and not account for scr refresh
            p_port_block1imageATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_block1imageATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_port_block1imageATT.started')
            p_port_block1imageATT.status = STARTED
            win.callOnFlip(p_port_block1imageATT.setData, int(COA1TT))
    
            # keep track of start time/frame for later
            #serialport.frameNStart = frameNB  # exact frame index
            #serialport.tStart = tB  # local t and not account for scr refresh
            #serialport.tStartRefresh = tThisFlipGlobalB  # on global time
            #winB.timeOnFlip(serialport, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(winB, 'serialport.started')
            #serialport.status = STARTED
            #winB.callOnFlip(serialport.write, bytes('pracCOB', 'utf8'))
            
            p_port_block1imageBTT.frameNStart = frameNB  # exact frame index
            p_port_block1imageBTT.tStart = tB  # local t and not account for scr refresh
            p_port_block1imageBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(p_port_block1imageBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'p_port_block1imageBTT.started')
            p_port_block1imageBTT.status = STARTED
            winB.callOnFlip(p_port_block1imageBTT.setData, int(COB1TT))
            
            
        if p_port_block1imageATT.status == STARTED and p_port_block1imageBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > p_port_block1imageATT.tStartRefresh + 0.1-frameTolerance) and (tThisFlipGlobalB > p_port_block1imageBTT.tStartRefresh + 0.1-frameTolerance):
                # keep track of stop time/frame for later
                p_port_block1imageATT.tStop = t  # not accounting for scr refresh
                p_port_block1imageATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'p_port_block1imageATT.stopped')
                p_port_block1imageATT.status = FINISHED
                win.callOnFlip(p_port_block1imageATT.setData, int(0))
                
                # keep track of stop time/frame for later
                #serialport.tStop = tB  # not accounting for scr refresh
                #serialport.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(winB, 'serialport.stopped')
                #serialport.status = FINISHED
                #winB.callOnFlip(serialport.write, bytes('0', 'utf8'))
                
                # keep track of stop time/frame for later
                p_port_block1imageBTT.tStop = tB  # not accounting for scr refresh
                p_port_block1imageBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'p_port_block1imageBTT.stopped')
                p_port_block1imageBTT.status = FINISHED
                winB.callOnFlip(p_port_block1imageBTT.setData, int(0))
        
        # *block1imageATT* *block1imageBTT* updates
        if block1imageATT.status == NOT_STARTED and block1imageBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block1imageATT.frameNStart = frameN  # exact frame index
            block1imageATT.tStart = t  # local t and not account for scr refresh
            block1imageATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block1imageATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block1imageATT.started')
            block1imageATT.setAutoDraw(True)
            # keep track of start time/frame for later
            block1imageBTT.frameNStart = frameNB  # exact frame index
            block1imageBTT.tStart = tB  # local t and not account for scr refresh
            block1imageBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block1imageBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block1imageBTT.started')
            block1imageBTT.setAutoDraw(True)
            
        if block1imageATT.status == STARTED and block1imageBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block1imageATT.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block1imageBTT.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block1imageATT.tStop = t  # not accounting for scr refresh
                block1imageATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block1imageATT.stopped')
                block1imageATT.setAutoDraw(False)
                # keep track of stop time/frame for later
                block1imageBTT.tStop = tB  # not accounting for scr refresh
                block1imageBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block1imageBTT.stopped')
                block1imageBTT.setAutoDraw(False)
        
        # *block1key_respTT* updates
        waitOnFlip = False
        if block1key_respTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block1key_respTT.frameNStart = frameN  # exact frame index
            block1key_respTT.tStart = t  # local t and not account for scr refresh
            block1key_respTT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block1key_respTT, 'tStartRefresh')  # time at next scr refresh
            winB.timeOnFlip(block1key_respTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block1key_respTT.started')
            thisExp.timestampOnFlip(winB, 'block1key_respTTB.started')
            block1key_respTT.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block1key_respTT.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block1key_respTT.clearEvents, eventType='keyboard')  # clear events on next screen flip
            winB.callOnFlip(block1key_respTT.clock.reset)  # t=0 on next screen flip
            winB.callOnFlip(block1key_respTT.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block1key_respTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block1key_respTT.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                block1key_respTT.tStop = t  # not accounting for scr refresh
                block1key_respTT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block1key_respTT.stopped')
                thisExp.timestampOnFlip(winB, 'block1key_respTTB.stopped')
                block1key_respTT.status = FINISHED
        if block1key_respTT.status == STARTED and not waitOnFlip:
            theseKeys = block1key_respTT.getKeys(keyList=['num_1','num_3','num_7','num_9'], waitRelease=False)
            _block1key_respTT_allKeys.extend(theseKeys)
            if len(_block1key_respTT_allKeys):
                block1key_respTT.keys = [key.name for key in _block1key_respTT_allKeys]  # storing all keys
                block1key_respTT.rt = [key.rt for key in _block1key_respTT_allKeys]
                # was this correct?
                if (block1key_respTT.keys == str(correctkey1TT)) or (block1key_respTT.keys == correctkey1TT):
                    block1key_respTT.corr = 1
                else:
                    block1key_respTT.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block1imageTTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block1imageTT" ---
    for thisComponent in block1imageTTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    if p_port_block1imageATT.status == STARTED:
        win.callOnFlip(p_port_block1imageATT.setData, int(0))
    if p_port_block1imageBTT.status == STARTED:
        winB.callOnFlip(p_port_block1imageBTT.setData, int(0))
    # check responses
    if block1key_respTT.keys in ['', [], None]:  # No response was made
        block1key_respTT.keys = None
        # was no response the correct answer?!
        if str(correctkey1TT).lower() == 'none':
           block1key_respTT.corr = 1;  # correct non-response
        else:
           block1key_respTT.corr = 0;  # failed to respond (incorrectly)
    # store data for block1TT (TrialHandler)
    block1TT.addData('block1key_respTT.keys',block1key_respTT.keys)
    block1TT.addData('block1key_respTT.corr', block1key_respTT.corr)
    if block1key_respTT.keys != None:  # we had a response
        block1TT.addData('block1key_respTT.rt', block1key_respTT.rt)
    # the Routine "block1imageTT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block1TT'


# --- Prepare to start Routine "block2instruction" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
# keep track of which components have finished
block2instructionComponents = [block2TextA, block2TextB]
for thisComponent in block2instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "block2instruction" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block2TextA* *block2TextB* updates
    if block2TextA.status == NOT_STARTED and block2TextB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block2TextA.frameNStart = frameN  # exact frame index
        block2TextA.tStart = t  # local t and not account for scr refresh
        block2TextA.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block2TextA, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'block2TextA.started')
        block2TextA.setAutoDraw(True)
        # keep track of start time/frame for later
        block2TextB.frameNStart = frameNB  # exact frame index
        block2TextB.tStart = tB  # local t and not account for scr refresh
        block2TextB.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(block2TextB, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'block2TextB.started')
        block2TextB.setAutoDraw(True)
        
    if block2TextA.status == STARTED and block2TextB.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if (tThisFlipGlobal > block2TextA.tStartRefresh + 10-frameTolerance) and (tThisFlipGlobalB > block2TextB.tStartRefresh + 10-frameTolerance):
            # keep track of stop time/frame for later
            block2TextA.tStop = t  # not accounting for scr refresh
            block2TextA.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block2TextA.stopped')
            block2TextA.setAutoDraw(False)
             # keep track of stop time/frame for later
            block2TextB.tStop = tB  # not accounting for scr refresh
            block2TextB.frameNStop = frameNB  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block1TextB.stopped')
            block2TextB.setAutoDraw(False)
            
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block2instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "block2instruction" ---
for thisComponent in block2instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
block2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('group1_b2.xlsx'),
    seed=None, name='block2')
thisExp.addLoop(block2)  # add the loop to the experiment
thisBlock2 = block2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock2.rgb)
if thisBlock2 != None:
    for paramName in thisBlock2:
        exec('{} = thisBlock2[paramName]'.format(paramName))

for thisBlock2 in block2:
    currentLoop = block2
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2.rgb)
    if thisBlock2 != None:
        for paramName in thisBlock2:
            exec('{} = thisBlock2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block2fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code2
    jitter = np.arange(1, 1.2, .10)
    shuffle(jitter)
    block2fixationA.setText('+')
    block2fixationB.setText('+')
    # keep track of which components have finished
    block2fixationComponents = [block2fixationA, block2fixationB]
    for thisComponent in block2fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block2fixation" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block2fixationA* *block2fixationB* updates
        if block2fixationA.status == NOT_STARTED and block2fixationB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block2fixationA.frameNStart = frameN  # exact frame index
            block2fixationA.tStart = t  # local t and not account for scr refresh
            block2fixationA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2fixationA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block2fixationA.started')
            block2fixationA.setAutoDraw(True)
            # keep track of start time/frame for later
            block2fixationB.frameNStart = frameNB  # exact frame index
            block2fixationB.tStart = tB  # local t and not account for scr refresh
            block2fixationB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block2fixationB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block2fixationB.started')
            block2fixationB.setAutoDraw(True)
        if block2fixationA.status == STARTED and block2fixationB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block2fixationA.tStartRefresh + jitter[0]-frameTolerance) and (tThisFlipGlobalB > block2fixationB.tStartRefresh + jitter[0]-frameTolerance):
                # keep track of stop time/frame for later
                block2fixationA.tStop = t  # not accounting for scr refresh
                block2fixationA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block1fixationA.stopped')
                block2fixationA.setAutoDraw(False)
                # keep track of stop time/frame for later
                block2fixationB.tStop = tB  # not accounting for scr refresh
                block2fixationB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block2fixationB.stopped')
                block2fixationB.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block2fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block2fixation" ---
    for thisComponent in block2fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    # the Routine "block2fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block2image" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    block2borderA.setImage(frameA2)
    block2imageA.setImage(imagesA2)
    block2key_resp.keys = []
    block2key_resp.rt = []
    _block2key_resp_allKeys = []
    block2borderB.setImage(frameB2)
    block2imageB.setImage(imagesB2)
    # keep track of which components have finished
    block2imageComponents = [p_port_block2imageA, p_port_block2imageB, block2borderA, block2imageA, block2key_resp, block2borderB, block2imageB]
    for thisComponent in block2imageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block2image" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_port_block2imageA* *p_port_block2imageB* updates
        if (p_port_block2imageA.status == NOT_STARTED and block2imageA.status == STARTED) and (p_port_block2imageB.status == NOT_STARTED and block2imageB.status == STARTED):
            # keep track of start time/frame for later
            p_port_block2imageA.frameNStart = frameN  # exact frame index
            p_port_block2imageA.tStart = t  # local t and not account for scr refresh
            p_port_block2imageA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_block2imageA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_port_block2imageA.started')
            p_port_block2imageA.status = STARTED
            win.callOnFlip(p_port_block2imageA.setData, int(COA2))
    
            # keep track of start time/frame for later
            #serialport.frameNStart = frameNB  # exact frame index
            #serialport.tStart = tB  # local t and not account for scr refresh
            #serialport.tStartRefresh = tThisFlipGlobalB  # on global time
            #winB.timeOnFlip(serialport, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(winB, 'serialport.started')
            #serialport.status = STARTED
            #winB.callOnFlip(serialport.write, bytes('pracCOB', 'utf8'))
            
            p_port_block2imageB.frameNStart = frameNB  # exact frame index
            p_port_block2imageB.tStart = tB  # local t and not account for scr refresh
            p_port_block2imageB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(p_port_block2imageB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'p_port_block2imageB.started')
            p_port_block2imageB.status = STARTED
            winB.callOnFlip(p_port_block2imageB.setData, int(COB2))
            
            
        if p_port_block2imageA.status == STARTED and p_port_block2imageB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > p_port_block2imageA.tStartRefresh + 0.1-frameTolerance) and (tThisFlipGlobalB > p_port_block2imageB.tStartRefresh + 0.1-frameTolerance):
                # keep track of stop time/frame for later
                p_port_block2imageA.tStop = t  # not accounting for scr refresh
                p_port_block2imageA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'p_port_block2imageA.stopped')
                p_port_block2imageA.status = FINISHED
                win.callOnFlip(p_port_block2imageA.setData, int(0))
                
                # keep track of stop time/frame for later
                #serialport.tStop = tB  # not accounting for scr refresh
                #serialport.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(winB, 'serialport.stopped')
                #serialport.status = FINISHED
                #winB.callOnFlip(serialport.write, bytes('0', 'utf8'))
                
                # keep track of stop time/frame for later
                p_port_block2imageB.tStop = tB  # not accounting for scr refresh
                p_port_block2imageB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'p_port_block2imageB.stopped')
                p_port_block2imageB.status = FINISHED
                winB.callOnFlip(p_port_block2imageB.setData, int(0))
        
        # *block2borderA* *block2borderB* updates
        if block2borderA.status == NOT_STARTED and block2borderB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block2borderA.frameNStart = frameN  # exact frame index
            block2borderA.tStart = t  # local t and not account for scr refresh
            block2borderA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2borderA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block2borderA.started')
            block2borderA.setAutoDraw(True)
            # keep track of start time/frame for later
            block2borderB.frameNStart = frameNB  # exact frame index
            block2borderB.tStart = tB  # local t and not account for scr refresh
            block2borderB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block2borderB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block2borderB.started')
            block2borderB.setAutoDraw(True)
            
        if block2borderA.status == STARTED and block2borderB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block2borderA.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block2borderB.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block2borderA.tStop = t  # not accounting for scr refresh
                block2borderA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block2borderA.stopped')
                block2borderA.setAutoDraw(False)
                # keep track of stop time/frame for later
                block2borderB.tStop = tB  # not accounting for scr refresh
                block2borderB.frameNStop = frameNB # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block2borderB.stopped')
                block2borderB.setAutoDraw(False)
        
        # *block2imageA* *block2imageB* updates
        if block2imageA.status == NOT_STARTED and block2imageB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block2imageA.frameNStart = frameN  # exact frame index
            block2imageA.tStart = t  # local t and not account for scr refresh
            block2imageA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2imageA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block2imageA.started')
            block2imageA.setAutoDraw(True)
            # keep track of start time/frame for later
            block2imageB.frameNStart = frameNB  # exact frame index
            block2imageB.tStart = tB  # local t and not account for scr refresh
            block2imageB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block2imageB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block2imageB.started')
            block2imageB.setAutoDraw(True)
            
        if block2imageA.status == STARTED and block2imageB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block2imageA.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block2imageB.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block2imageA.tStop = t  # not accounting for scr refresh
                block2imageA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block2imageA.stopped')
                block2imageA.setAutoDraw(False)
                 # keep track of stop time/frame for later
                block2imageB.tStop = tB  # not accounting for scr refresh
                block2imageB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block2imageB.stopped')
                block2imageB.setAutoDraw(False)
        
        # *block2key_resp* updates
        waitOnFlip = False
        if block2key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block2key_resp.frameNStart = frameN  # exact frame index
            block2key_resp.tStart = t  # local t and not account for scr refresh
            block2key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2key_resp, 'tStartRefresh')  # time at next scr refresh
            winB.timeOnFlip(block2key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block2key_resp.started')
            thisExp.timestampOnFlip(winB, 'block2key_respB.started')
            block2key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block2key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block2key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            winB.callOnFlip(block2key_resp.clock.reset)  # t=0 on next screen flip
            winB.callOnFlip(block2key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block2key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block2key_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                block2key_resp.tStop = t  # not accounting for scr refresh
                block2key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block2key_resp.stopped')
                thisExp.timestampOnFlip(winB, 'block2key_respB.stopped')
                block2key_resp.status = FINISHED
        if block2key_resp.status == STARTED and not waitOnFlip:
            theseKeys = block2key_resp.getKeys(keyList=['num_1','num_3','num_7','num_9'], waitRelease=False)
            _block2key_resp_allKeys.extend(theseKeys)
            if len(_block2key_resp_allKeys):
                block2key_resp.keys = [key.name for key in _block2key_resp_allKeys]  # storing all keys
                block2key_resp.rt = [key.rt for key in _block2key_resp_allKeys]
                # was this correct?
                if (block2key_resp.keys == str(correctkey2)) or (prac_key_resp.keys == correctkey2):
                    block2key_resp.corr = 1
                else:
                    block2key_resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block2imageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block2image" ---
    for thisComponent in block2imageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    if p_port_block2imageA.status == STARTED:
        win.callOnFlip(p_port_block2imageA.setData, int(0))
    if p_port_block2imageB.status == STARTED:
        winB.callOnFlip(p_port_block2imageB.setData, int(0))
    # check responses
    if block2key_resp.keys in ['', [], None]:  # No response was made
        block2key_resp.keys = None
        # was no response the correct answer?!
        if str(correctkey2).lower() == 'none':
           block2key_resp.corr = 1;  # correct non-response
        else:
           block2key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for block2 (TrialHandler)
    block2.addData('block2key_resp.keys',block2key_resp.keys)
    block2.addData('block2key_resp.corr', block2key_resp.corr)
    if block2key_resp.keys != None:  # we had a response
        block2.addData('block2key_resp.rt', block2key_resp.rt)
    # the Routine "block2image" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block2'


# --- Prepare to start Routine "block2instructionTT" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
# keep track of which components have finished
block2instructionTTComponents = [block2TextATT, block2TextBTT]
for thisComponent in block2instructionTTComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "block2instructionTT" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
    
    # *block2TextATT* *block2TextBTT* updates
    if block2TextATT.status == NOT_STARTED and block2TextBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block2TextATT.frameNStart = frameN  # exact frame index
        block2TextATT.tStart = t  # local t and not account for scr refresh
        block2TextATT.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block2TextATT, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'block2TextATT.started')
        block2TextATT.setAutoDraw(True)
        # keep track of start time/frame for later
        block2TextBTT.frameNStart = frameNB  # exact frame index
        block2TextBTT.tStart = tB  # local t and not account for scr refresh
        block2TextBTT.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(block2TextBTT, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'block2TextBTT.started')
        block2TextBTT.setAutoDraw(True)
        
    if block2TextATT.status == STARTED and block2TextBTT.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if (tThisFlipGlobal > block2TextATT.tStartRefresh + 10-frameTolerance) and (tThisFlipGlobalB > block2TextBTT.tStartRefresh + 10-frameTolerance):
            # keep track of stop time/frame for later
            block2TextATT.tStop = t  # not accounting for scr refresh
            block2TextATT.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block2TextATT.stopped')
            block2TextATT.setAutoDraw(False)
            # keep track of stop time/frame for later
            block2TextBTT.tStop = tB  # not accounting for scr refresh
            block2TextBTT.frameNStop = frameNB  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block2TextBTT.stopped')
            block2TextBTT.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block2instructionTTComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "block2instructionTT" ---
for thisComponent in block2instructionTTComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
block2TT = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('group1_b2TT.xlsx'),
    seed=None, name='block2TT')
thisExp.addLoop(block2TT)  # add the loop to the experiment
thisBlock2TT = block2TT.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock2TT.rgb)
if thisBlock2TT != None:
    for paramName in thisBlock2TT:
        exec('{} = thisBlock2TT[paramName]'.format(paramName))

for thisBlock2TT in block2TT:
    currentLoop = block2TT
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2TT.rgb)
    if thisBlock2TT != None:
        for paramName in thisBlock2TT:
            exec('{} = thisBlock2TT[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block2fixationTT" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code2TT
    jitter = np.arange(1, 1.2, .10)
    shuffle(jitter)
    block2fixationATT.setText('+')
    block2fixationBTT.setText('+')
    # keep track of which components have finished
    block2fixationTTComponents = [block2fixationATT, block2fixationBTT]
    for thisComponent in block2fixationTTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block2fixationTT" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block2fixationATT* *block2fixationBTT* updates
        if block2fixationATT.status == NOT_STARTED and block2fixationBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block2fixationATT.frameNStart = frameN  # exact frame index
            block2fixationATT.tStart = t  # local t and not account for scr refresh
            block2fixationATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2fixationATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block2fixationATT.started')
            block2fixationATT.setAutoDraw(True)
            # keep track of start time/frame for later
            block2fixationBTT.frameNStart = frameNB  # exact frame index
            block2fixationBTT.tStart = tB  # local t and not account for scr refresh
            block2fixationBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block2fixationBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block2fixationBTT.started')
            block2fixationBTT.setAutoDraw(True)
        
        if block2fixationATT.status == STARTED and block2fixationBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block2fixationATT.tStartRefresh + jitter[0]-frameTolerance) and (tThisFlipGlobalB > block2fixationBTT.tStartRefresh + jitter[0]-frameTolerance):
                # keep track of stop time/frame for later
                block2fixationATT.tStop = t  # not accounting for scr refresh
                block2fixationATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block2fixationATT.stopped')
                block2fixationATT.setAutoDraw(False)
                # keep track of stop time/frame for later
                block2fixationBTT.tStop = tB  # not accounting for scr refresh
                block2fixationBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block2fixationBTT.stopped')
                block2fixationBTT.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block2fixationTTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block2fixationTT" ---
    for thisComponent in block2fixationTTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    # the Routine "block2fixationTT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block2imageTT" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    block2imageATT.setImage(imagesA2TT)
    block2key_respTT.keys = []
    block2key_respTT.rt = []
    _block2key_respTT_allKeys = []
    block2imageBTT.setImage(imagesB2TT)
    # keep track of which components have finished
    block2imageTTComponents = [p_port_block2imageATT, p_port_block2imageBTT, block2imageATT, block2key_respTT, block2imageBTT]
    for thisComponent in block2imageTTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block2imageTT" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_port_block2imageA* *p_port_block2imageB* updates
        if (p_port_block2imageATT.status == NOT_STARTED and block2imageATT.status == STARTED) and (p_port_block2imageBTT.status == NOT_STARTED and block2imageBTT.status == STARTED):
            # keep track of start time/frame for later
            p_port_block2imageATT.frameNStart = frameN  # exact frame index
            p_port_block2imageATT.tStart = t  # local t and not account for scr refresh
            p_port_block2imageATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_block2imageATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_port_block2imageATT.started')
            p_port_block2imageATT.status = STARTED
            win.callOnFlip(p_port_block2imageATT.setData, int(COA2TT))
    
            # keep track of start time/frame for later
            #serialport.frameNStart = frameNB  # exact frame index
            #serialport.tStart = tB  # local t and not account for scr refresh
            #serialport.tStartRefresh = tThisFlipGlobalB  # on global time
            #winB.timeOnFlip(serialport, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(winB, 'serialport.started')
            #serialport.status = STARTED
            #winB.callOnFlip(serialport.write, bytes('pracCOB', 'utf8'))
            
            p_port_block2imageBTT.frameNStart = frameNB  # exact frame index
            p_port_block2imageBTT.tStart = tB  # local t and not account for scr refresh
            p_port_block2imageBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(p_port_block2imageBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'p_port_block2imageBTT.started')
            p_port_block2imageBTT.status = STARTED
            winB.callOnFlip(p_port_block2imageBTT.setData, int(COB2TT))
            
            
        if p_port_block2imageATT.status == STARTED and p_port_block2imageBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > p_port_block2imageATT.tStartRefresh + 0.1-frameTolerance) and (tThisFlipGlobalB > p_port_block2imageBTT.tStartRefresh + 0.1-frameTolerance):
                # keep track of stop time/frame for later
                p_port_block2imageATT.tStop = t  # not accounting for scr refresh
                p_port_block2imageATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'p_port_block2imageATT.stopped')
                p_port_block2imageATT.status = FINISHED
                win.callOnFlip(p_port_block2imageATT.setData, int(0))
                
                # keep track of stop time/frame for later
                #serialport.tStop = tB  # not accounting for scr refresh
                #serialport.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(winB, 'serialport.stopped')
                #serialport.status = FINISHED
                #winB.callOnFlip(serialport.write, bytes('0', 'utf8'))
                
                # keep track of stop time/frame for later
                p_port_block2imageBTT.tStop = tB  # not accounting for scr refresh
                p_port_block2imageBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'p_port_block2imageBTT.stopped')
                p_port_block2imageBTT.status = FINISHED
                winB.callOnFlip(p_port_block2imageBTT.setData, int(0))
        
        # *block2imageATT* *block2imageBTT* updates
        if block2imageATT.status == NOT_STARTED and block2imageBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block2imageATT.frameNStart = frameN  # exact frame index
            block2imageATT.tStart = t  # local t and not account for scr refresh
            block2imageATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2imageATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block2imageATT.started')
            block2imageATT.setAutoDraw(True)
            # keep track of start time/frame for later
            block2imageBTT.frameNStart = frameNB  # exact frame index
            block2imageBTT.tStart = tB  # local t and not account for scr refresh
            block2imageBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block2imageBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block2imageBTT.started')
            block2imageBTT.setAutoDraw(True)
            
        if block2imageATT.status == STARTED and block2imageBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block2imageATT.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block2imageBTT.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block2imageATT.tStop = t  # not accounting for scr refresh
                block2imageATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block2imageATT.stopped')
                block2imageATT.setAutoDraw(False)
                # keep track of stop time/frame for later
                block2imageBTT.tStop = tB  # not accounting for scr refresh
                block2imageBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block2imageBTT.stopped')
                block2imageBTT.setAutoDraw(False)
        
        # *block2key_respTT* updates
        waitOnFlip = False
        if block2key_respTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block2key_respTT.frameNStart = frameN  # exact frame index
            block2key_respTT.tStart = t  # local t and not account for scr refresh
            block2key_respTT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2key_respTT, 'tStartRefresh')  # time at next scr refresh
            winB.timeOnFlip(block2key_respTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block2key_respTT.started')
            thisExp.timestampOnFlip(winB, 'block2key_respTTB.started')
            block2key_respTT.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block2key_respTT.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block2key_respTT.clearEvents, eventType='keyboard')  # clear events on next screen flip
            winB.callOnFlip(block2key_respTT.clock.reset)  # t=0 on next screen flip
            winB.callOnFlip(block2key_respTT.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block2key_respTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block2key_respTT.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                block2key_respTT.tStop = t  # not accounting for scr refresh
                block2key_respTT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block2key_respTT.stopped')
                thisExp.timestampOnFlip(winB, 'block2key_respTTB.stopped')
                block2key_respTT.status = FINISHED
        if block2key_respTT.status == STARTED and not waitOnFlip:
            theseKeys = block2key_respTT.getKeys(keyList=['num_1','num_3','num_7','num_9'], waitRelease=False)
            _block2key_respTT_allKeys.extend(theseKeys)
            if len(_block2key_respTT_allKeys):
                block2key_respTT.keys = [key.name for key in _block2key_respTT_allKeys]  # storing all keys
                block2key_respTT.rt = [key.rt for key in _block2key_respTT_allKeys]
                # was this correct?
                if (block2key_respTT.keys == str(correctkey2TT)) or (block2key_respTT.keys == correctkey2TT):
                    block2key_respTT.corr = 1
                else:
                    block2key_respTT.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block2imageTTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block2imageTT" ---
    for thisComponent in block2imageTTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    if p_port_block2imageATT.status == STARTED:
        win.callOnFlip(p_port_block2imageATT.setData, int(0))
    if p_port_block2imageBTT.status == STARTED:
        winB.callOnFlip(p_port_block2imageBTT.setData, int(0))
    # check responses
    if block2key_respTT.keys in ['', [], None]:  # No response was made
        block2key_respTT.keys = None
        # was no response the correct answer?!
        if str(correctkey2TT).lower() == 'none':
           block2key_respTT.corr = 1;  # correct non-response
        else:
           block2key_respTT.corr = 0;  # failed to respond (incorrectly)
    # store data for block2TT (TrialHandler)
    block2TT.addData('block2key_respTT.keys',block2key_respTT.keys)
    block2TT.addData('block2key_respTT.corr', block2key_respTT.corr)
    if block2key_respTT.keys != None:  # we had a response
        block2TT.addData('block2key_respTT.rt', block2key_respTT.rt)
    # the Routine "block2imageTT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block2TT'


# --- Prepare to start Routine "block3instruction" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
# keep track of which components have finished
block3instructionComponents = [block3TextA, block3TextB]
for thisComponent in block3instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "block3instruction" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block3TextA* *block3TextB* updates
    if block3TextA.status == NOT_STARTED and block3TextB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block3TextA.frameNStart = frameN  # exact frame index
        block3TextA.tStart = t  # local t and not account for scr refresh
        block3TextA.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block3TextA, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'block3TextA.started')
        block3TextA.setAutoDraw(True)
        # keep track of start time/frame for later
        block3TextB.frameNStart = frameNB  # exact frame index
        block3TextB.tStart = tB  # local t and not account for scr refresh
        block3TextB.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(block3TextB, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'block3TextB.started')
        block3TextB.setAutoDraw(True)
        
    if block3TextA.status == STARTED and block3TextB.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if (tThisFlipGlobal > block3TextA.tStartRefresh + 10-frameTolerance) and (tThisFlipGlobalB > block3TextB.tStartRefresh + 10-frameTolerance):
            # keep track of stop time/frame for later
            block3TextA.tStop = t  # not accounting for scr refresh
            block3TextA.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block3TextA.stopped')
            block3TextA.setAutoDraw(False)
             # keep track of stop time/frame for later
            block3TextB.tStop = tB  # not accounting for scr refresh
            block3TextB.frameNStop = frameNB  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block3TextB.stopped')
            block3TextB.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block3instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "block3instruction" ---
for thisComponent in block3instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
block3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('group1_b3.xlsx'),
    seed=None, name='block3')
thisExp.addLoop(block3)  # add the loop to the experiment
thisBlock3 = block3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock3.rgb)
if thisBlock3 != None:
    for paramName in thisBlock3:
        exec('{} = thisBlock3[paramName]'.format(paramName))

for thisBlock3 in block3:
    currentLoop = block3
    # abbreviate parameter names if possible (e.g. rgb = thisBlock3.rgb)
    if thisBlock3 != None:
        for paramName in thisBlock3:
            exec('{} = thisBlock3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block3fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code3
    jitter = np.arange(1, 1.2, .10)
    shuffle(jitter)
    block3fixationA.setText('+')
    block3fixationB.setText('+')
    # keep track of which components have finished
    block3fixationComponents = [block3fixationA, block3fixationB]
    for thisComponent in block3fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block3fixation" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block3fixationA* *block3fixationB* updates
        if block3fixationA.status == NOT_STARTED and block3fixationB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3fixationA.frameNStart = frameN  # exact frame index
            block3fixationA.tStart = t  # local t and not account for scr refresh
            block3fixationA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3fixationA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block3fixationA.started')
            block3fixationA.setAutoDraw(True)
            # keep track of start time/frame for later
            block3fixationB.frameNStart = frameNB  # exact frame index
            block3fixationB.tStart = tB  # local t and not account for scr refresh
            block3fixationB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block3fixationB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block3fixationB.started')
            block3fixationB.setAutoDraw(True)
        if block3fixationA.status == STARTED and block3fixationB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block3fixationA.tStartRefresh + jitter[0]-frameTolerance) and (tThisFlipGlobalB > block3fixationB.tStartRefresh + jitter[0]-frameTolerance):
                # keep track of stop time/frame for later
                block3fixationA.tStop = t  # not accounting for scr refresh
                block3fixationA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block3fixationA.stopped')
                block3fixationA.setAutoDraw(False)
                # keep track of stop time/frame for later
                block3fixationB.tStop = tB  # not accounting for scr refresh
                block3fixationB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block3fixationB.stopped')
                block3fixationB.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block3fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block3fixation" ---
    for thisComponent in block3fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    # the Routine "block3fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block3image" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    block3borderA.setImage(frameA3)
    block3imageA.setImage(imagesA3)
    block3key_resp.keys = []
    block3key_resp.rt = []
    _block3key_resp_allKeys = []
    block3borderB.setImage(frameB3)
    block3imageB.setImage(imagesB3)
    # keep track of which components have finished
    block3imageComponents = [p_port_block3imageA, p_port_block3imageB, block3borderA, block3imageA, block3key_resp, block3borderB, block3imageB]
    for thisComponent in block3imageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block3image" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_port_block3imageA* *p_port_block3imageB* updates
        if (p_port_block3imageA.status == NOT_STARTED and block3imageA.status == STARTED) and (p_port_block3imageB.status == NOT_STARTED and block3imageB.status == STARTED):
            # keep track of start time/frame for later
            p_port_block3imageA.frameNStart = frameN  # exact frame index
            p_port_block3imageA.tStart = t  # local t and not account for scr refresh
            p_port_block3imageA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_block3imageA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_port_block3imageA.started')
            p_port_block3imageA.status = STARTED
            win.callOnFlip(p_port_block3imageA.setData, int(COA3))
    
            # keep track of start time/frame for later
            #serialport.frameNStart = frameNB  # exact frame index
            #serialport.tStart = tB  # local t and not account for scr refresh
            #serialport.tStartRefresh = tThisFlipGlobalB  # on global time
            #winB.timeOnFlip(serialport, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(winB, 'serialport.started')
            #serialport.status = STARTED
            #winB.callOnFlip(serialport.write, bytes('pracCOB', 'utf8'))
            
            p_port_block3imageB.frameNStart = frameNB  # exact frame index
            p_port_block3imageB.tStart = tB  # local t and not account for scr refresh
            p_port_block3imageB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(p_port_block3imageB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'p_port_block3imageB.started')
            p_port_block3imageB.status = STARTED
            winB.callOnFlip(p_port_block3imageB.setData, int(COB3))
            
            
        if p_port_block3imageA.status == STARTED and p_port_block3imageB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > p_port_block3imageA.tStartRefresh + 0.1-frameTolerance) and (tThisFlipGlobalB > p_port_block3imageB.tStartRefresh + 0.1-frameTolerance):
                # keep track of stop time/frame for later
                p_port_block3imageA.tStop = t  # not accounting for scr refresh
                p_port_block3imageA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'p_port_block3imageA.stopped')
                p_port_block3imageA.status = FINISHED
                win.callOnFlip(p_port_block3imageA.setData, int(0))
                
                # keep track of stop time/frame for later
                #serialport.tStop = tB  # not accounting for scr refresh
                #serialport.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(winB, 'serialport.stopped')
                #serialport.status = FINISHED
                #winB.callOnFlip(serialport.write, bytes('0', 'utf8'))
                
                # keep track of stop time/frame for later
                p_port_block3imageB.tStop = tB  # not accounting for scr refresh
                p_port_block3imageB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'p_port_block3imageB.stopped')
                p_port_block3imageB.status = FINISHED
                winB.callOnFlip(p_port_block3imageB.setData, int(0))
        
        # *block3borderA* *block3borderB* updates
        if block3borderA.status == NOT_STARTED and block3borderB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3borderA.frameNStart = frameN  # exact frame index
            block3borderA.tStart = t  # local t and not account for scr refresh
            block3borderA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3borderA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block3borderA.started')
            block3borderA.setAutoDraw(True)
            # keep track of start time/frame for later
            block3borderB.frameNStart = frameNB  # exact frame index
            block3borderB.tStart = tB  # local t and not account for scr refresh
            block3borderB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block3borderB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block3borderB.started')
            block3borderB.setAutoDraw(True)
            
        if block3borderA.status == STARTED and block3borderB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block3borderA.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block3borderB.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block3borderA.tStop = t  # not accounting for scr refresh
                block3borderA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block3borderA.stopped')
                block3borderA.setAutoDraw(False)
                # keep track of stop time/frame for later
                block3borderB.tStop = tB  # not accounting for scr refresh
                block3borderB.frameNStop = frameNB # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block3borderB.stopped')
                block3borderB.setAutoDraw(False)
        
        # *block3imageA* *block3imageB* updates
        if block3imageA.status == NOT_STARTED and block3imageB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3imageA.frameNStart = frameN  # exact frame index
            block3imageA.tStart = t  # local t and not account for scr refresh
            block3imageA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3imageA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block3imageA.started')
            block3imageA.setAutoDraw(True)
            # keep track of start time/frame for later
            block3imageB.frameNStart = frameNB  # exact frame index
            block3imageB.tStart = tB  # local t and not account for scr refresh
            block3imageB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block3imageB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block3imageB.started')
            block3imageB.setAutoDraw(True)
            
        if block3imageA.status == STARTED and block3imageB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block3imageA.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block3imageB.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block3imageA.tStop = t  # not accounting for scr refresh
                block3imageA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block3imageA.stopped')
                block3imageA.setAutoDraw(False)
                 # keep track of stop time/frame for later
                block3imageB.tStop = tB  # not accounting for scr refresh
                block3imageB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block3imageB.stopped')
                block3imageB.setAutoDraw(False)
        
        # *block3key_resp* updates
        waitOnFlip = False
        if block3key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3key_resp.frameNStart = frameN  # exact frame index
            block3key_resp.tStart = t  # local t and not account for scr refresh
            block3key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3key_resp, 'tStartRefresh')  # time at next scr refresh
            winB.timeOnFlip(block3key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block3key_resp.started')
            thisExp.timestampOnFlip(winB, 'block3key_respB.started')
            block3key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block3key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block3key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            winB.callOnFlip(block3key_resp.clock.reset)  # t=0 on next screen flip
            winB.callOnFlip(block3key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block3key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block3key_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                block3key_resp.tStop = t  # not accounting for scr refresh
                block3key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block3key_resp.stopped')
                thisExp.timestampOnFlip(winB, 'block3key_respB.stopped')
                block3key_resp.status = FINISHED
        if block3key_resp.status == STARTED and not waitOnFlip:
            theseKeys = block3key_resp.getKeys(keyList=['num_1','num_3','num_7','num_9'], waitRelease=False)
            _block3key_resp_allKeys.extend(theseKeys)
            if len(_block3key_resp_allKeys):
                block3key_resp.keys = [key.name for key in _block3key_resp_allKeys]  # storing all keys
                block3key_resp.rt = [key.rt for key in _block3key_resp_allKeys]
                # was this correct?
                if (block3key_resp.keys == str(correctkey3)) or (prac_key_resp.keys == correctkey3):
                    block3key_resp.corr = 1
                else:
                    block3key_resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block3imageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block3image" ---
    for thisComponent in block3imageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    if p_port_block3imageA.status == STARTED:
        win.callOnFlip(p_port_block3imageA.setData, int(0))
    if p_port_block3imageB.status == STARTED:
        winB.callOnFlip(p_port_block3imageB.setData, int(0))
    # check responses
    if block3key_resp.keys in ['', [], None]:  # No response was made
        block3key_resp.keys = None
        # was no response the correct answer?!
        if str(correctkey3).lower() == 'none':
           block3key_resp.corr = 1;  # correct non-response
        else:
           block3key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for block3 (TrialHandler)
    block3.addData('block3key_resp.keys',block3key_resp.keys)
    block3.addData('block3key_resp.corr', block3key_resp.corr)
    if block3key_resp.keys != None:  # we had a response
        block3.addData('block3key_resp.rt', block3key_resp.rt)
    # the Routine "block3image" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block3'


# --- Prepare to start Routine "block3instructionTT" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
# keep track of which components have finished
block3instructionTTComponents = [block3TextATT, block3TextBTT]
for thisComponent in block3instructionTTComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "block3instructionTT" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block3TextATT* *block3TextBTT* updates
    if block3TextATT.status == NOT_STARTED and block3TextBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block3TextATT.frameNStart = frameN  # exact frame index
        block3TextATT.tStart = t  # local t and not account for scr refresh
        block3TextATT.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block3TextATT, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'block3TextATT.started')
        block3TextATT.setAutoDraw(True)
        # keep track of start time/frame for later
        block3TextBTT.frameNStart = frameNB  # exact frame index
        block3TextBTT.tStart = tB  # local t and not account for scr refresh
        block3TextBTT.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(block3TextBTT, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'block3TextBTT.started')
        block3TextBTT.setAutoDraw(True)
        
    if block3TextATT.status == STARTED and block3TextBTT.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if (tThisFlipGlobal > block3TextATT.tStartRefresh + 10-frameTolerance) and (tThisFlipGlobalB > block3TextBTT.tStartRefresh + 10-frameTolerance):
            # keep track of stop time/frame for later
            block3TextATT.tStop = t  # not accounting for scr refresh
            block3TextATT.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block3TextATT.stopped')
            block3TextATT.setAutoDraw(False)
            # keep track of stop time/frame for later
            block3TextBTT.tStop = tB  # not accounting for scr refresh
            block3TextBTT.frameNStop = frameNB  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block3TextBTT.stopped')
            block3TextBTT.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block3instructionTTComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "block3instructionTT" ---
for thisComponent in block3instructionTTComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
block3TT = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('group1_b3TT.xlsx'),
    seed=None, name='block3TT')
thisExp.addLoop(block3TT)  # add the loop to the experiment
thisBlock3TT = block3TT.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock3TT.rgb)
if thisBlock3TT != None:
    for paramName in thisBlock3TT:
        exec('{} = thisBlock3TT[paramName]'.format(paramName))

for thisBlock3TT in block3TT:
    currentLoop = block3TT
    # abbreviate parameter names if possible (e.g. rgb = thisBlock3TT.rgb)
    if thisBlock3TT != None:
        for paramName in thisBlock3TT:
            exec('{} = thisBlock3TT[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block3fixationTT" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code3TT
    jitter = np.arange(1, 1.2, .10)
    shuffle(jitter)
    block3fixationATT.setText('+')
    block3fixationBTT.setText('+')
    # keep track of which components have finished
    block3fixationTTComponents = [block3fixationATT, block3fixationBTT]
    for thisComponent in block3fixationTTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block3fixationTT" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block3fixationATT* *block3fixationBTT* updates
        if block3fixationATT.status == NOT_STARTED and block3fixationBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3fixationATT.frameNStart = frameN  # exact frame index
            block3fixationATT.tStart = t  # local t and not account for scr refresh
            block3fixationATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3fixationATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block3fixationATT.started')
            block3fixationATT.setAutoDraw(True)
            # keep track of start time/frame for later
            block3fixationBTT.frameNStart = frameNB  # exact frame index
            block3fixationBTT.tStart = tB  # local t and not account for scr refresh
            block3fixationBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block3fixationBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block3fixationBTT.started')
            block3fixationBTT.setAutoDraw(True)
        
        if block3fixationATT.status == STARTED and block3fixationBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block3fixationATT.tStartRefresh + jitter[0]-frameTolerance) and (tThisFlipGlobalB > block3fixationBTT.tStartRefresh + jitter[0]-frameTolerance):
                # keep track of stop time/frame for later
                block3fixationATT.tStop = t  # not accounting for scr refresh
                block3fixationATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block3fixationATT.stopped')
                block3fixationATT.setAutoDraw(False)
                # keep track of stop time/frame for later
                block3fixationBTT.tStop = tB  # not accounting for scr refresh
                block3fixationBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block3fixationBTT.stopped')
                block3fixationBTT.setAutoDraw(False)
                
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block3fixationTTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block3fixationTT" ---
    for thisComponent in block3fixationTTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    # the Routine "block3fixationTT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block3imageTT" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    block3imageATT.setImage(imagesA3TT)
    block3key_respTT.keys = []
    block3key_respTT.rt = []
    _block3key_respTT_allKeys = []
    block3imageBTT.setImage(imagesB3TT)
    # keep track of which components have finished
    block3imageTTComponents = [p_port_block3imageATT, p_port_block3imageBTT, block3imageATT, block3key_respTT, block3imageBTT]
    for thisComponent in block3imageTTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block3imageTT" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_port_block3imageA* *p_port_block3imageB* updates
        if (p_port_block3imageATT.status == NOT_STARTED and block3imageATT.status == STARTED) and (p_port_block3imageBTT.status == NOT_STARTED and block3imageBTT.status == STARTED):
            # keep track of start time/frame for later
            p_port_block3imageATT.frameNStart = frameN  # exact frame index
            p_port_block3imageATT.tStart = t  # local t and not account for scr refresh
            p_port_block3imageATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_block3imageATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_port_block3imageATT.started')
            p_port_block3imageATT.status = STARTED
            win.callOnFlip(p_port_block3imageATT.setData, int(COA3TT))
    
            # keep track of start time/frame for later
            #serialport.frameNStart = frameNB  # exact frame index
            #serialport.tStart = tB  # local t and not account for scr refresh
            #serialport.tStartRefresh = tThisFlipGlobalB  # on global time
            #winB.timeOnFlip(serialport, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(winB, 'serialport.started')
            #serialport.status = STARTED
            #winB.callOnFlip(serialport.write, bytes('pracCOB', 'utf8'))
            
            p_port_block3imageBTT.frameNStart = frameNB  # exact frame index
            p_port_block3imageBTT.tStart = tB  # local t and not account for scr refresh
            p_port_block3imageBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(p_port_block3imageBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'p_port_block3imageBTT.started')
            p_port_block3imageBTT.status = STARTED
            winB.callOnFlip(p_port_block3imageBTT.setData, int(COB3TT))
            
            
        if p_port_block3imageATT.status == STARTED and p_port_block3imageBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > p_port_block3imageATT.tStartRefresh + 0.1-frameTolerance) and (tThisFlipGlobalB > p_port_block3imageBTT.tStartRefresh + 0.1-frameTolerance):
                # keep track of stop time/frame for later
                p_port_block3imageATT.tStop = t  # not accounting for scr refresh
                p_port_block3imageATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'p_port_block3imageATT.stopped')
                p_port_block3imageATT.status = FINISHED
                win.callOnFlip(p_port_block3imageATT.setData, int(0))
                
                # keep track of stop time/frame for later
                #serialport.tStop = tB  # not accounting for scr refresh
                #serialport.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(winB, 'serialport.stopped')
                #serialport.status = FINISHED
                #winB.callOnFlip(serialport.write, bytes('0', 'utf8'))
                
                # keep track of stop time/frame for later
                p_port_block3imageBTT.tStop = tB  # not accounting for scr refresh
                p_port_block3imageBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'p_port_block3imageBTT.stopped')
                p_port_block3imageBTT.status = FINISHED
                winB.callOnFlip(p_port_block3imageBTT.setData, int(0))
        
        # *block3imageATT* *block3imageBTT* updates
        if block3imageATT.status == NOT_STARTED and block3imageBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3imageATT.frameNStart = frameN  # exact frame index
            block3imageATT.tStart = t  # local t and not account for scr refresh
            block3imageATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3imageATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block3imageATT.started')
            block3imageATT.setAutoDraw(True)
            # keep track of start time/frame for later
            block3imageBTT.frameNStart = frameNB  # exact frame index
            block3imageBTT.tStart = tB  # local t and not account for scr refresh
            block3imageBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block3imageBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block3imageBTT.started')
            block3imageBTT.setAutoDraw(True)
            
        if block3imageATT.status == STARTED and block3imageBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block3imageATT.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block3imageBTT.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block3imageATT.tStop = t  # not accounting for scr refresh
                block3imageATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block3imageATT.stopped')
                block3imageATT.setAutoDraw(False)
                # keep track of stop time/frame for later
                block3imageBTT.tStop = tB  # not accounting for scr refresh
                block3imageBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block3imageBTT.stopped')
                block3imageBTT.setAutoDraw(False)
        
        # *block3key_respTT* updates
        waitOnFlip = False
        if block3key_respTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3key_respTT.frameNStart = frameN  # exact frame index
            block3key_respTT.tStart = t  # local t and not account for scr refresh
            block3key_respTT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3key_respTT, 'tStartRefresh')  # time at next scr refresh
            winB.timeOnFlip(block3key_respTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block3key_respTT.started')
            thisExp.timestampOnFlip(winB, 'block3key_respTTB.started')
            block3key_respTT.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block3key_respTT.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block3key_respTT.clearEvents, eventType='keyboard')  # clear events on next screen flip
            winB.callOnFlip(block3key_respTT.clock.reset)  # t=0 on next screen flip
            winB.callOnFlip(block3key_respTT.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block3key_respTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block3key_respTT.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                block3key_respTT.tStop = t  # not accounting for scr refresh
                block3key_respTT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block3key_respTT.stopped')
                thisExp.timestampOnFlip(winB, 'block3key_respTTB.stopped')
                block3key_respTT.status = FINISHED
        if block3key_respTT.status == STARTED and not waitOnFlip:
            theseKeys = block3key_respTT.getKeys(keyList=['num_1','num_3','num_7','num_9'], waitRelease=False)
            _block3key_respTT_allKeys.extend(theseKeys)
            if len(_block3key_respTT_allKeys):
                block3key_respTT.keys = [key.name for key in _block3key_respTT_allKeys]  # storing all keys
                block3key_respTT.rt = [key.rt for key in _block3key_respTT_allKeys]
                # was this correct?
                if (block3key_respTT.keys == str(correctkey3TT)) or (block3key_respTT.keys == correctkey3TT):
                    block3key_respTT.corr = 1
                else:
                    block3key_respTT.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block3imageTTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block3imageTT" ---
    for thisComponent in block3imageTTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    if p_port_block3imageATT.status == STARTED:
        win.callOnFlip(p_port_block3imageATT.setData, int(0))
    if p_port_block3imageBTT.status == STARTED:
        winB.callOnFlip(p_port_block3imageBTT.setData, int(0))
    # check responses
    if block3key_respTT.keys in ['', [], None]:  # No response was made
        block3key_respTT.keys = None
        # was no response the correct answer?!
        if str(correctkey3TT).lower() == 'none':
           block3key_respTT.corr = 1;  # correct non-response
        else:
           block3key_respTT.corr = 0;  # failed to respond (incorrectly)
    # store data for block3TT (TrialHandler)
    block3TT.addData('block3key_respTT.keys',block3key_respTT.keys)
    block3TT.addData('block3key_respTT.corr', block3key_respTT.corr)
    if block3key_respTT.keys != None:  # we had a response
        block3TT.addData('block3key_respTT.rt', block3key_respTT.rt)
    # the Routine "block3imageTT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block3TT'


# --- Prepare to start Routine "mainbreak" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
# keep track of which components have finished
mainbreakComponents = [breakTextA, breakTextB]
for thisComponent in mainbreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "mainbreak" ---
while continueRoutine and routineTimer.getTime() < 30.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *breakTextA* updates
    if breakTextA.status == NOT_STARTED and breakTextB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        breakTextA.frameNStart = frameN  # exact frame index
        breakTextA.tStart = t  # local t and not account for scr refresh
        breakTextA.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(breakTextA, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'breakTextA.started')
        breakTextA.setAutoDraw(True)
        # keep track of start time/frame for later
        breakTextB.frameNStart = frameNB  # exact frame index
        breakTextB.tStart = tB  # local t and not account for scr refresh
        breakTextB.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(breakTextB, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'breakTextB.started')
        breakTextB.setAutoDraw(True)
        
    if breakTextA.status == STARTED and breakTextB.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if (tThisFlipGlobal > breakTextA.tStartRefresh + 30-frameTolerance) and (tThisFlipGlobalB > breakTextB.tStartRefresh + 30-frameTolerance):
            # keep track of stop time/frame for later
            breakTextA.tStop = t  # not accounting for scr refresh
            breakTextA.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'breakTextA.stopped')
            breakTextA.setAutoDraw(False)
             # keep track of stop time/frame for later
            breakTextB.tStop = tB  # not accounting for scr refresh
            breakTextB.frameNStop = frameNB  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'breakTextB.stopped')
            breakTextB.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mainbreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "mainbreak" ---
for thisComponent in mainbreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-30.000000)

# --- Prepare to start Routine "block4instruction" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
# keep track of which components have finished
block4instructionComponents = [block4TextA, block4TextB]
for thisComponent in block4instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "block4instruction" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block4TextA* *block4TextB* updates
    if block4TextA.status == NOT_STARTED and block4TextB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block4TextA.frameNStart = frameN  # exact frame index
        block4TextA.tStart = t  # local t and not account for scr refresh
        block4TextA.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block4TextA, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'block4TextA.started')
        block4TextA.setAutoDraw(True)
        # keep track of start time/frame for later
        block4TextB.frameNStart = frameNB  # exact frame index
        block4TextB.tStart = tB  # local t and not account for scr refresh
        block4TextB.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(block4TextB, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'block4TextB.started')
        block4TextB.setAutoDraw(True)
        
    if block4TextA.status == STARTED and block4TextB.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if (tThisFlipGlobal > block4TextA.tStartRefresh + 10-frameTolerance) and (tThisFlipGlobalB > block4TextB.tStartRefresh + 10-frameTolerance):
            # keep track of stop time/frame for later
            block4TextA.tStop = t  # not accounting for scr refresh
            block4TextA.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block4TextA.stopped')
            block4TextA.setAutoDraw(False)
             # keep track of stop time/frame for later
            block4TextB.tStop = tB  # not accounting for scr refresh
            block4TextB.frameNStop = frameNB  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block4TextB.stopped')
            block4TextB.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block4instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "block4instruction" ---
for thisComponent in block4instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
block4 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('group1_b4.xlsx'),
    seed=None, name='block4')
thisExp.addLoop(block4)  # add the loop to the experiment
thisBlock4 = block4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock4.rgb)
if thisBlock4 != None:
    for paramName in thisBlock4:
        exec('{} = thisBlock4[paramName]'.format(paramName))

for thisBlock4 in block4:
    currentLoop = block4
    # abbreviate parameter names if possible (e.g. rgb = thisBlock4.rgb)
    if thisBlock4 != None:
        for paramName in thisBlock4:
            exec('{} = thisBlock4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block4fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code4
    jitter = np.arange(1, 1.2, .10)
    shuffle(jitter)
    block4fixationA.setText('+')
    block4fixationB.setText('+')
    # keep track of which components have finished
    block4fixationComponents = [block4fixationA, block4fixationB]
    for thisComponent in block4fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block4fixation" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block4fixationA* *block4fixationB* updates
        if block4fixationA.status == NOT_STARTED and block4fixationB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block4fixationA.frameNStart = frameN  # exact frame index
            block4fixationA.tStart = t  # local t and not account for scr refresh
            block4fixationA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block4fixationA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block4fixationA.started')
            block4fixationA.setAutoDraw(True)
            # keep track of start time/frame for later
            block4fixationB.frameNStart = frameNB  # exact frame index
            block4fixationB.tStart = tB  # local t and not account for scr refresh
            block4fixationB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block4fixationB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block4fixationB.started')
            block4fixationB.setAutoDraw(True)
        if block4fixationA.status == STARTED and block4fixationB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block4fixationA.tStartRefresh + jitter[0]-frameTolerance) and (tThisFlipGlobalB > block4fixationB.tStartRefresh + jitter[0]-frameTolerance):
                # keep track of stop time/frame for later
                block4fixationA.tStop = t  # not accounting for scr refresh
                block4fixationA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block4fixationA.stopped')
                block4fixationA.setAutoDraw(False)
                # keep track of stop time/frame for later
                block4fixationB.tStop = tB  # not accounting for scr refresh
                block4fixationB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block4fixationB.stopped')
                block4fixationB.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block4fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block4fixation" ---
    for thisComponent in block4fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    # the Routine "block4fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block4image" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    block4borderA.setImage(frameA4)
    block4imageA.setImage(imagesA4)
    block4key_resp.keys = []
    block4key_resp.rt = []
    _block4key_resp_allKeys = []
    block4borderB.setImage(frameB4)
    block4imageB.setImage(imagesB4)
    # keep track of which components have finished
    block4imageComponents = [p_port_block4imageA, p_port_block4imageB, block4borderA, block4imageA, block4key_resp, block4borderB, block4imageB]
    for thisComponent in block4imageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block4image" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_port_block4imageA* *p_port_block4imageB* updates
        if (p_port_block4imageA.status == NOT_STARTED and block4imageA.status == STARTED) and (p_port_block4imageB.status == NOT_STARTED and block4imageB.status == STARTED):
            # keep track of start time/frame for later
            p_port_block4imageA.frameNStart = frameN  # exact frame index
            p_port_block4imageA.tStart = t  # local t and not account for scr refresh
            p_port_block4imageA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_block4imageA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_port_block4imageA.started')
            p_port_block4imageA.status = STARTED
            win.callOnFlip(p_port_block4imageA.setData, int(COA4))
    
            # keep track of start time/frame for later
            #serialport.frameNStart = frameNB  # exact frame index
            #serialport.tStart = tB  # local t and not account for scr refresh
            #serialport.tStartRefresh = tThisFlipGlobalB  # on global time
            #winB.timeOnFlip(serialport, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(winB, 'serialport.started')
            #serialport.status = STARTED
            #winB.callOnFlip(serialport.write, bytes('pracCOB', 'utf8'))
            
            p_port_block4imageB.frameNStart = frameNB  # exact frame index
            p_port_block4imageB.tStart = tB  # local t and not account for scr refresh
            p_port_block4imageB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(p_port_block4imageB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'p_port_block4imageB.started')
            p_port_block4imageB.status = STARTED
            winB.callOnFlip(p_port_block4imageB.setData, int(COB4))
            
            
        if p_port_block4imageA.status == STARTED and p_port_block4imageB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > p_port_block4imageA.tStartRefresh + 0.1-frameTolerance) and (tThisFlipGlobalB > p_port_block4imageB.tStartRefresh + 0.1-frameTolerance):
                # keep track of stop time/frame for later
                p_port_block4imageA.tStop = t  # not accounting for scr refresh
                p_port_block4imageA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'p_port_block4imageA.stopped')
                p_port_block4imageA.status = FINISHED
                win.callOnFlip(p_port_block4imageA.setData, int(0))
                
                # keep track of stop time/frame for later
                #serialport.tStop = tB  # not accounting for scr refresh
                #serialport.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(winB, 'serialport.stopped')
                #serialport.status = FINISHED
                #winB.callOnFlip(serialport.write, bytes('0', 'utf8'))
                
                # keep track of stop time/frame for later
                p_port_block4imageB.tStop = tB  # not accounting for scr refresh
                p_port_block4imageB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'p_port_block4imageB.stopped')
                p_port_block4imageB.status = FINISHED
                winB.callOnFlip(p_port_block4imageB.setData, int(0))
        
        # *block4borderA* *block4borderB* updates
        if block4borderA.status == NOT_STARTED and block4borderB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block4borderA.frameNStart = frameN  # exact frame index
            block4borderA.tStart = t  # local t and not account for scr refresh
            block4borderA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block4borderA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block4borderA.started')
            block4borderA.setAutoDraw(True)
            # keep track of start time/frame for later
            block4borderB.frameNStart = frameNB  # exact frame index
            block4borderB.tStart = tB  # local t and not account for scr refresh
            block4borderB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block4borderB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block4borderB.started')
            block4borderB.setAutoDraw(True)
            
        if block4borderA.status == STARTED and block4borderB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block4borderA.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block4borderB.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block4borderA.tStop = t  # not accounting for scr refresh
                block4borderA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block4borderA.stopped')
                block4borderA.setAutoDraw(False)
                # keep track of stop time/frame for later
                block4borderB.tStop = tB  # not accounting for scr refresh
                block4borderB.frameNStop = frameNB # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block4borderB.stopped')
                block4borderB.setAutoDraw(False)
        
        # *block4imageA* *block4imageB* updates
        if block4imageA.status == NOT_STARTED and block4imageB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block4imageA.frameNStart = frameN  # exact frame index
            block4imageA.tStart = t  # local t and not account for scr refresh
            block4imageA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block4imageA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block4imageA.started')
            block4imageA.setAutoDraw(True)
            # keep track of start time/frame for later
            block4imageB.frameNStart = frameNB  # exact frame index
            block4imageB.tStart = tB  # local t and not account for scr refresh
            block4imageB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block4imageB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block4imageB.started')
            block4imageB.setAutoDraw(True)
            
        if block4imageA.status == STARTED and block4imageB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block4imageA.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block4imageB.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block4imageA.tStop = t  # not accounting for scr refresh
                block4imageA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block4imageA.stopped')
                block4imageA.setAutoDraw(False)
                 # keep track of stop time/frame for later
                block4imageB.tStop = tB  # not accounting for scr refresh
                block4imageB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block4imageB.stopped')
                block4imageB.setAutoDraw(False)
        
        # *block4key_resp* updates
        waitOnFlip = False
        if block4key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block4key_resp.frameNStart = frameN  # exact frame index
            block4key_resp.tStart = t  # local t and not account for scr refresh
            block4key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block4key_resp, 'tStartRefresh')  # time at next scr refresh
            winB.timeOnFlip(block4key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block4key_resp.started')
            thisExp.timestampOnFlip(winB, 'block4key_respB.started')
            block4key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block4key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block4key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            winB.callOnFlip(block4key_resp.clock.reset)  # t=0 on next screen flip
            winB.callOnFlip(block4key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block4key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block4key_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                block4key_resp.tStop = t  # not accounting for scr refresh
                block4key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block4key_resp.stopped')
                thisExp.timestampOnFlip(winB, 'block4key_respB.stopped')
                block4key_resp.status = FINISHED
        if block4key_resp.status == STARTED and not waitOnFlip:
            theseKeys = block4key_resp.getKeys(keyList=['num_1','num_3','num_7','num_9'], waitRelease=False)
            _block4key_resp_allKeys.extend(theseKeys)
            if len(_block4key_resp_allKeys):
                block4key_resp.keys = [key.name for key in _block4key_resp_allKeys]  # storing all keys
                block4key_resp.rt = [key.rt for key in _block4key_resp_allKeys]
                # was this correct?
                if (block4key_resp.keys == str(correctkey4)) or (prac_key_resp.keys == correctkey4):
                    block4key_resp.corr = 1
                else:
                    block4key_resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block4imageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block4image" ---
    for thisComponent in block4imageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    if p_port_block4imageA.status == STARTED:
        win.callOnFlip(p_port_block4imageA.setData, int(0))
    if p_port_block4imageB.status == STARTED:
        winB.callOnFlip(p_port_block4imageB.setData, int(0))
    # check responses
    if block4key_resp.keys in ['', [], None]:  # No response was made
        block4key_resp.keys = None
        # was no response the correct answer?!
        if str(correctkey4).lower() == 'none':
           block4key_resp.corr = 1;  # correct non-response
        else:
           block4key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for block4 (TrialHandler)
    block4.addData('block4key_resp.keys',block4key_resp.keys)
    block4.addData('block4key_resp.corr', block4key_resp.corr)
    if block4key_resp.keys != None:  # we had a response
        block4.addData('block4key_resp.rt', block4key_resp.rt)
    # the Routine "block4image" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block4'


# --- Prepare to start Routine "block4instructionTT" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
# keep track of which components have finished
block4instructionTTComponents = [block4TextATT, block4TextBTT]
for thisComponent in block4instructionTTComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "block4instructionTT" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block4TextATT* *block4TextBTT* updates
    if block4TextATT.status == NOT_STARTED and block4TextBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block4TextATT.frameNStart = frameN  # exact frame index
        block4TextATT.tStart = t  # local t and not account for scr refresh
        block4TextATT.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block4TextATT, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'block4TextATT.started')
        block4TextATT.setAutoDraw(True)
        # keep track of start time/frame for later
        block4TextBTT.frameNStart = frameNB  # exact frame index
        block4TextBTT.tStart = tB  # local t and not account for scr refresh
        block4TextBTT.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(block4TextBTT, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'block4TextBTT.started')
        block4TextBTT.setAutoDraw(True)
        
    if block4TextATT.status == STARTED and block4TextBTT.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if (tThisFlipGlobal > block4TextATT.tStartRefresh + 10-frameTolerance) and (tThisFlipGlobalB > block4TextBTT.tStartRefresh + 10-frameTolerance):
            # keep track of stop time/frame for later
            block4TextATT.tStop = t  # not accounting for scr refresh
            block4TextATT.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block4TextATT.stopped')
            block4TextATT.setAutoDraw(False)
            # keep track of stop time/frame for later
            block4TextBTT.tStop = tB  # not accounting for scr refresh
            block4TextBTT.frameNStop = frameNB  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block4TextBTT.stopped')
            block4TextBTT.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block4instructionTTComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "block4instructionTT" ---
for thisComponent in block4instructionTTComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
block4TT = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('group1_b4TT.xlsx'),
    seed=None, name='block4TT')
thisExp.addLoop(block4TT)  # add the loop to the experiment
thisBlock4TT = block4TT.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock4TT.rgb)
if thisBlock4TT != None:
    for paramName in thisBlock4TT:
        exec('{} = thisBlock4TT[paramName]'.format(paramName))

for thisBlock4TT in block4TT:
    currentLoop = block4TT
    # abbreviate parameter names if possible (e.g. rgb = thisBlock4TT.rgb)
    if thisBlock4TT != None:
        for paramName in thisBlock4TT:
            exec('{} = thisBlock4TT[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block4fixationTT" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code4TT
    jitter = np.arange(1, 1.2, .10)
    shuffle(jitter)
    block4fixationATT.setText('+')
    block4fixationBTT.setText('+')
    # keep track of which components have finished
    block4fixationTTComponents = [block4fixationATT, block4fixationBTT]
    for thisComponent in block4fixationTTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block4fixationTT" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block4fixationATT* *block4fixationBTT* updates
        if block4fixationATT.status == NOT_STARTED and block4fixationBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block4fixationATT.frameNStart = frameN  # exact frame index
            block4fixationATT.tStart = t  # local t and not account for scr refresh
            block4fixationATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block4fixationATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block4fixationATT.started')
            block4fixationATT.setAutoDraw(True)
            # keep track of start time/frame for later
            block4fixationBTT.frameNStart = frameNB  # exact frame index
            block4fixationBTT.tStart = tB  # local t and not account for scr refresh
            block4fixationBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block4fixationBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block4fixationBTT.started')
            block4fixationBTT.setAutoDraw(True)
        
        if block4fixationATT.status == STARTED and block4fixationBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block4fixationATT.tStartRefresh + jitter[0]-frameTolerance) and (tThisFlipGlobalB > block4fixationBTT.tStartRefresh + jitter[0]-frameTolerance):
                # keep track of stop time/frame for later
                block4fixationATT.tStop = t  # not accounting for scr refresh
                block4fixationATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block4fixationATT.stopped')
                block4fixationATT.setAutoDraw(False)
                # keep track of stop time/frame for later
                block4fixationBTT.tStop = tB  # not accounting for scr refresh
                block4fixationBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block4fixationBTT.stopped')
                block4fixationBTT.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block4fixationTTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block4fixationTT" ---
    for thisComponent in block4fixationTTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    # the Routine "block4fixationTT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block4imageTT" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    block4imageATT.setImage(imagesA4TT)
    block4key_respTT.keys = []
    block4key_respTT.rt = []
    _block4key_respTT_allKeys = []
    block4imageBTT.setImage(imagesB4TT)
    # keep track of which components have finished
    block4imageTTComponents = [p_port_block4imageATT, p_port_block4imageBTT, block4imageATT, block4key_respTT, block4imageBTT]
    for thisComponent in block4imageTTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block4imageTT" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_port_block4imageA* *p_port_block4imageB* updates
        if (p_port_block4imageATT.status == NOT_STARTED and block4imageATT.status == STARTED) and (p_port_block4imageBTT.status == NOT_STARTED and block4imageBTT.status == STARTED):
            # keep track of start time/frame for later
            p_port_block4imageATT.frameNStart = frameN  # exact frame index
            p_port_block4imageATT.tStart = t  # local t and not account for scr refresh
            p_port_block4imageATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_block4imageATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_port_block4imageATT.started')
            p_port_block4imageATT.status = STARTED
            win.callOnFlip(p_port_block4imageATT.setData, int(COA4TT))
    
            # keep track of start time/frame for later
            #serialport.frameNStart = frameNB  # exact frame index
            #serialport.tStart = tB  # local t and not account for scr refresh
            #serialport.tStartRefresh = tThisFlipGlobalB  # on global time
            #winB.timeOnFlip(serialport, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(winB, 'serialport.started')
            #serialport.status = STARTED
            #winB.callOnFlip(serialport.write, bytes('pracCOB', 'utf8'))
            
            p_port_block4imageBTT.frameNStart = frameNB  # exact frame index
            p_port_block4imageBTT.tStart = tB  # local t and not account for scr refresh
            p_port_block4imageBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(p_port_block4imageBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'p_port_block4imageBTT.started')
            p_port_block4imageBTT.status = STARTED
            winB.callOnFlip(p_port_block4imageBTT.setData, int(COB4TT))
            
            
        if p_port_block4imageATT.status == STARTED and p_port_block4imageBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > p_port_block4imageATT.tStartRefresh + 0.1-frameTolerance) and (tThisFlipGlobalB > p_port_block4imageBTT.tStartRefresh + 0.1-frameTolerance):
                # keep track of stop time/frame for later
                p_port_block4imageATT.tStop = t  # not accounting for scr refresh
                p_port_block4imageATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'p_port_block4imageATT.stopped')
                p_port_block4imageATT.status = FINISHED
                win.callOnFlip(p_port_block4imageATT.setData, int(0))
                
                # keep track of stop time/frame for later
                #serialport.tStop = tB  # not accounting for scr refresh
                #serialport.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(winB, 'serialport.stopped')
                #serialport.status = FINISHED
                #winB.callOnFlip(serialport.write, bytes('0', 'utf8'))
                
                # keep track of stop time/frame for later
                p_port_block4imageBTT.tStop = tB  # not accounting for scr refresh
                p_port_block4imageBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'p_port_block4imageBTT.stopped')
                p_port_block4imageBTT.status = FINISHED
                winB.callOnFlip(p_port_block4imageBTT.setData, int(0))
        
        # *block4imageATT* *block4imageBTT* updates
        if block4imageATT.status == NOT_STARTED and block4imageBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block4imageATT.frameNStart = frameN  # exact frame index
            block4imageATT.tStart = t  # local t and not account for scr refresh
            block4imageATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block4imageATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block4imageATT.started')
            block4imageATT.setAutoDraw(True)
            # keep track of start time/frame for later
            block4imageBTT.frameNStart = frameNB  # exact frame index
            block4imageBTT.tStart = tB  # local t and not account for scr refresh
            block4imageBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block4imageBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block4imageBTT.started')
            block4imageBTT.setAutoDraw(True)
            
        if block4imageATT.status == STARTED and block4imageBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block4imageATT.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block4imageBTT.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block4imageATT.tStop = t  # not accounting for scr refresh
                block4imageATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block4imageATT.stopped')
                block4imageATT.setAutoDraw(False)
                # keep track of stop time/frame for later
                block4imageBTT.tStop = tB  # not accounting for scr refresh
                block4imageBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block4imageBTT.stopped')
                block4imageBTT.setAutoDraw(False)
        
        # *block4key_respTT* updates
        waitOnFlip = False
        if block4key_respTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block4key_respTT.frameNStart = frameN  # exact frame index
            block4key_respTT.tStart = t  # local t and not account for scr refresh
            block4key_respTT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block4key_respTT, 'tStartRefresh')  # time at next scr refresh
            winB.timeOnFlip(block4key_respTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block4key_respTT.started')
            thisExp.timestampOnFlip(winB, 'block4key_respTTB.started')
            block4key_respTT.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block4key_respTT.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block4key_respTT.clearEvents, eventType='keyboard')  # clear events on next screen flip
            winB.callOnFlip(block4key_respTT.clock.reset)  # t=0 on next screen flip
            winB.callOnFlip(block4key_respTT.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block4key_respTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block4key_respTT.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                block4key_respTT.tStop = t  # not accounting for scr refresh
                block4key_respTT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block4key_respTT.stopped')
                thisExp.timestampOnFlip(winB, 'block4key_respTTB.stopped')
                block4key_respTT.status = FINISHED
        if block4key_respTT.status == STARTED and not waitOnFlip:
            theseKeys = block4key_respTT.getKeys(keyList=['num_1','num_3','num_7','num_9'], waitRelease=False)
            _block4key_respTT_allKeys.extend(theseKeys)
            if len(_block4key_respTT_allKeys):
                block4key_respTT.keys = [key.name for key in _block4key_respTT_allKeys]  # storing all keys
                block4key_respTT.rt = [key.rt for key in _block4key_respTT_allKeys]
                # was this correct?
                if (block4key_respTT.keys == str(correctkey4TT)) or (block4key_respTT.keys == correctkey4TT):
                    block4key_respTT.corr = 1
                else:
                    block4key_respTT.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block4imageTTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block4imageTT" ---
    for thisComponent in block4imageTTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    if p_port_block4imageATT.status == STARTED:
        win.callOnFlip(p_port_block4imageATT.setData, int(0))
    if p_port_block4imageBTT.status == STARTED:
        winB.callOnFlip(p_port_block4imageBTT.setData, int(0))
    # check responses
    if block4key_respTT.keys in ['', [], None]:  # No response was made
        block4key_respTT.keys = None
        # was no response the correct answer?!
        if str(correctkey4TT).lower() == 'none':
           block4key_respTT.corr = 1;  # correct non-response
        else:
           block4key_respTT.corr = 0;  # failed to respond (incorrectly)
    # store data for block4TT (TrialHandler)
    block4TT.addData('block4key_respTT.keys',block4key_respTT.keys)
    block4TT.addData('block4key_respTT.corr', block4key_respTT.corr)
    if block4key_respTT.keys != None:  # we had a response
        block4TT.addData('block4key_respTT.rt', block4key_respTT.rt)
    # the Routine "block4imageTT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block4TT'


# --- Prepare to start Routine "block5instruction" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
# keep track of which components have finished
block5instructionComponents = [block5TextA, block5TextB]
for thisComponent in block5instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "block5instruction" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block5TextA* *block5TextB* updates
    if block5TextA.status == NOT_STARTED and block5TextB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block5TextA.frameNStart = frameN  # exact frame index
        block5TextA.tStart = t  # local t and not account for scr refresh
        block5TextA.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block5TextA, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'block5TextA.started')
        block5TextA.setAutoDraw(True)
        # keep track of start time/frame for later
        block5TextB.frameNStart = frameNB  # exact frame index
        block5TextB.tStart = tB  # local t and not account for scr refresh
        block5TextB.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(block5TextB, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'block5TextB.started')
        block5TextB.setAutoDraw(True)
        
    if block5TextA.status == STARTED and block5TextB.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if (tThisFlipGlobal > block5TextA.tStartRefresh + 10-frameTolerance) and (tThisFlipGlobalB > block5TextB.tStartRefresh + 10-frameTolerance):
            # keep track of stop time/frame for later
            block5TextA.tStop = t  # not accounting for scr refresh
            block5TextA.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block5TextA.stopped')
            block5TextA.setAutoDraw(False)
             # keep track of stop time/frame for later
            block5TextB.tStop = tB  # not accounting for scr refresh
            block5TextB.frameNStop = frameNB  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block5TextB.stopped')
            block5TextB.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block5instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "block5instruction" ---
for thisComponent in block5instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
block5 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('group1_b5.xlsx'),
    seed=None, name='block5')
thisExp.addLoop(block5)  # add the loop to the experiment
thisBlock5 = block5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock5.rgb)
if thisBlock5 != None:
    for paramName in thisBlock5:
        exec('{} = thisBlock5[paramName]'.format(paramName))

for thisBlock5 in block5:
    currentLoop = block5
    # abbreviate parameter names if possible (e.g. rgb = thisBlock5.rgb)
    if thisBlock5 != None:
        for paramName in thisBlock5:
            exec('{} = thisBlock5[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block5fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code5
    jitter = np.arange(1, 1.2, .10)
    shuffle(jitter)
    block5fixationA.setText('+')
    block5fixationB.setText('+')
    # keep track of which components have finished
    block5fixationComponents = [block5fixationA, block5fixationB]
    for thisComponent in block5fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block5fixation" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block5fixationA* *block5fixationB* updates
        if block5fixationA.status == NOT_STARTED and block5fixationB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block5fixationA.frameNStart = frameN  # exact frame index
            block5fixationA.tStart = t  # local t and not account for scr refresh
            block5fixationA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block5fixationA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block5fixationA.started')
            block5fixationA.setAutoDraw(True)
            # keep track of start time/frame for later
            block5fixationB.frameNStart = frameNB  # exact frame index
            block5fixationB.tStart = tB  # local t and not account for scr refresh
            block5fixationB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block5fixationB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block5fixationB.started')
            block5fixationB.setAutoDraw(True)
        if block5fixationA.status == STARTED and block5fixationB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block5fixationA.tStartRefresh + jitter[0]-frameTolerance) and (tThisFlipGlobalB > block5fixationB.tStartRefresh + jitter[0]-frameTolerance):
                # keep track of stop time/frame for later
                block5fixationA.tStop = t  # not accounting for scr refresh
                block5fixationA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block5fixationA.stopped')
                block5fixationA.setAutoDraw(False)
                # keep track of stop time/frame for later
                block5fixationB.tStop = tB  # not accounting for scr refresh
                block5fixationB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block5fixationB.stopped')
                block5fixationB.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block5fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block5fixation" ---
    for thisComponent in block5fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    # the Routine "block5fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block5image" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    block5borderA.setImage(frameA5)
    block5imageA.setImage(imagesA5)
    block5key_resp.keys = []
    block5key_resp.rt = []
    _block5key_resp_allKeys = []
    block5borderB.setImage(frameB5)
    block5imageB.setImage(imagesB5)
    # keep track of which components have finished
    block5imageComponents = [p_port_block5imageA, p_port_block5imageB, block5borderA, block5imageA, block5key_resp, block5borderB, block5imageB]
    for thisComponent in block5imageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block5image" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_port_block5imageA* *p_port_block5imageB* updates
        if (p_port_block5imageA.status == NOT_STARTED and block5imageA.status == STARTED) and (p_port_block5imageB.status == NOT_STARTED and block5imageB.status == STARTED):
            # keep track of start time/frame for later
            p_port_block5imageA.frameNStart = frameN  # exact frame index
            p_port_block5imageA.tStart = t  # local t and not account for scr refresh
            p_port_block5imageA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_block5imageA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_port_block5imageA.started')
            p_port_block5imageA.status = STARTED
            win.callOnFlip(p_port_block5imageA.setData, int(COA5))
    
            # keep track of start time/frame for later
            #serialport.frameNStart = frameNB  # exact frame index
            #serialport.tStart = tB  # local t and not account for scr refresh
            #serialport.tStartRefresh = tThisFlipGlobalB  # on global time
            #winB.timeOnFlip(serialport, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(winB, 'serialport.started')
            #serialport.status = STARTED
            #winB.callOnFlip(serialport.write, bytes('pracCOB', 'utf8'))
            
            p_port_block5imageB.frameNStart = frameNB  # exact frame index
            p_port_block5imageB.tStart = tB  # local t and not account for scr refresh
            p_port_block5imageB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(p_port_block5imageB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'p_port_block5imageB.started')
            p_port_block5imageB.status = STARTED
            winB.callOnFlip(p_port_block5imageB.setData, int(COB5))
            
            
        if p_port_block5imageA.status == STARTED and p_port_block5imageB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > p_port_block5imageA.tStartRefresh + 0.1-frameTolerance) and (tThisFlipGlobalB > p_port_block5imageB.tStartRefresh + 0.1-frameTolerance):
                # keep track of stop time/frame for later
                p_port_block5imageA.tStop = t  # not accounting for scr refresh
                p_port_block5imageA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'p_port_block5imageA.stopped')
                p_port_block5imageA.status = FINISHED
                win.callOnFlip(p_port_block5imageA.setData, int(0))
                
                # keep track of stop time/frame for later
                #serialport.tStop = tB  # not accounting for scr refresh
                #serialport.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(winB, 'serialport.stopped')
                #serialport.status = FINISHED
                #winB.callOnFlip(serialport.write, bytes('0', 'utf8'))
                
                # keep track of stop time/frame for later
                p_port_block5imageB.tStop = tB  # not accounting for scr refresh
                p_port_block5imageB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'p_port_block5imageB.stopped')
                p_port_block5imageB.status = FINISHED
                winB.callOnFlip(p_port_block5imageB.setData, int(0))
        
        # *block5borderA* *block5borderB* updates
        if block5borderA.status == NOT_STARTED and block5borderB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block5borderA.frameNStart = frameN  # exact frame index
            block5borderA.tStart = t  # local t and not account for scr refresh
            block5borderA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block5borderA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block5borderA.started')
            block5borderA.setAutoDraw(True)
            # keep track of start time/frame for later
            block5borderB.frameNStart = frameNB  # exact frame index
            block5borderB.tStart = tB  # local t and not account for scr refresh
            block5borderB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block5borderB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block5borderB.started')
            block5borderB.setAutoDraw(True)
            
        if block5borderA.status == STARTED and block5borderB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block5borderA.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block5borderB.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block5borderA.tStop = t  # not accounting for scr refresh
                block5borderA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block5borderA.stopped')
                block5borderA.setAutoDraw(False)
                # keep track of stop time/frame for later
                block5borderB.tStop = tB  # not accounting for scr refresh
                block5borderB.frameNStop = frameNB # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block5borderB.stopped')
                block5borderB.setAutoDraw(False)
        
        # *block5imageA* *block5imageB* updates
        if block5imageA.status == NOT_STARTED and block5imageB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block5imageA.frameNStart = frameN  # exact frame index
            block5imageA.tStart = t  # local t and not account for scr refresh
            block5imageA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block5imageA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block5imageA.started')
            block5imageA.setAutoDraw(True)
            # keep track of start time/frame for later
            block5imageB.frameNStart = frameNB  # exact frame index
            block5imageB.tStart = tB  # local t and not account for scr refresh
            block5imageB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block5imageB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block5imageB.started')
            block5imageB.setAutoDraw(True)
            
        if block5imageA.status == STARTED and block5imageB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block5imageA.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block5imageB.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block5imageA.tStop = t  # not accounting for scr refresh
                block5imageA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block5imageA.stopped')
                block5imageA.setAutoDraw(False)
                 # keep track of stop time/frame for later
                block5imageB.tStop = tB  # not accounting for scr refresh
                block5imageB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block5imageB.stopped')
                block5imageB.setAutoDraw(False)
        
        # *block5key_resp* updates
        waitOnFlip = False
        if block5key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block5key_resp.frameNStart = frameN  # exact frame index
            block5key_resp.tStart = t  # local t and not account for scr refresh
            block5key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block5key_resp, 'tStartRefresh')  # time at next scr refresh
            winB.timeOnFlip(block5key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block5key_resp.started')
            thisExp.timestampOnFlip(winB, 'block5key_respB.started')
            block5key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block5key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block5key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            winB.callOnFlip(block5key_resp.clock.reset)  # t=0 on next screen flip
            winB.callOnFlip(block5key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block5key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block5key_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                block5key_resp.tStop = t  # not accounting for scr refresh
                block5key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block5key_resp.stopped')
                thisExp.timestampOnFlip(winB, 'block5key_respB.stopped')
                block5key_resp.status = FINISHED
        if block5key_resp.status == STARTED and not waitOnFlip:
            theseKeys = block5key_resp.getKeys(keyList=['num_1','num_3','num_7','num_9'], waitRelease=False)
            _block5key_resp_allKeys.extend(theseKeys)
            if len(_block5key_resp_allKeys):
                block5key_resp.keys = [key.name for key in _block5key_resp_allKeys]  # storing all keys
                block5key_resp.rt = [key.rt for key in _block5key_resp_allKeys]
                # was this correct?
                if (block5key_resp.keys == str(correctkey5)) or (prac_key_resp.keys == correctkey5):
                    block5key_resp.corr = 1
                else:
                    block5key_resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block5imageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block5image" ---
    for thisComponent in block5imageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    if p_port_block5imageA.status == STARTED:
        win.callOnFlip(p_port_block5imageA.setData, int(0))
    if p_port_block5imageB.status == STARTED:
        winB.callOnFlip(p_port_block5imageB.setData, int(0))
    # check responses
    if block5key_resp.keys in ['', [], None]:  # No response was made
        block5key_resp.keys = None
        # was no response the correct answer?!
        if str(correctkey5).lower() == 'none':
           block5key_resp.corr = 1;  # correct non-response
        else:
           block5key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for block5 (TrialHandler)
    block5.addData('block5key_resp.keys',block5key_resp.keys)
    block5.addData('block5key_resp.corr', block5key_resp.corr)
    if block5key_resp.keys != None:  # we had a response
        block5.addData('block5key_resp.rt', block5key_resp.rt)
    # the Routine "block5image" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block5'


# --- Prepare to start Routine "block5instructionTT" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
# keep track of which components have finished
block5instructionTTComponents = [block5TextATT, block5TextBTT]
for thisComponent in block5instructionTTComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "block5instructionTT" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block5TextATT* *block5TextBTT* updates
    if block5TextATT.status == NOT_STARTED and block5TextBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block5TextATT.frameNStart = frameN  # exact frame index
        block5TextATT.tStart = t  # local t and not account for scr refresh
        block5TextATT.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block5TextATT, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'block5TextATT.started')
        block5TextATT.setAutoDraw(True)
        # keep track of start time/frame for later
        block5TextBTT.frameNStart = frameNB  # exact frame index
        block5TextBTT.tStart = tB  # local t and not account for scr refresh
        block5TextBTT.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(block5TextBTT, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'block5TextBTT.started')
        block5TextBTT.setAutoDraw(True)
        
    if block5TextATT.status == STARTED and block5TextBTT.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if (tThisFlipGlobal > block5TextATT.tStartRefresh + 10-frameTolerance) and (tThisFlipGlobalB > block5TextBTT.tStartRefresh + 10-frameTolerance):
            # keep track of stop time/frame for later
            block5TextATT.tStop = t  # not accounting for scr refresh
            block5TextATT.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block5TextATT.stopped')
            block5TextATT.setAutoDraw(False)
            # keep track of stop time/frame for later
            block5TextBTT.tStop = tB  # not accounting for scr refresh
            block5TextBTT.frameNStop = frameNB  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block5TextBTT.stopped')
            block5TextBTT.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block5instructionTTComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "block5instructionTT" ---
for thisComponent in block5instructionTTComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
block5TT = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('group1_b5TT.xlsx'),
    seed=None, name='block5TT')
thisExp.addLoop(block5TT)  # add the loop to the experiment
thisBlock5TT = block5TT.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock5TT.rgb)
if thisBlock5TT != None:
    for paramName in thisBlock5TT:
        exec('{} = thisBlock5TT[paramName]'.format(paramName))

for thisBlock5TT in block5TT:
    currentLoop = block5TT
    # abbreviate parameter names if possible (e.g. rgb = thisBlock5TT.rgb)
    if thisBlock5TT != None:
        for paramName in thisBlock5TT:
            exec('{} = thisBlock5TT[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block5fixationTT" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code5TT
    jitter = np.arange(1, 1.2, .10)
    shuffle(jitter)
    block5fixationATT.setText('+')
    block5fixationBTT.setText('+')
    # keep track of which components have finished
    block5fixationTTComponents = [block5fixationATT, block5fixationBTT]
    for thisComponent in block5fixationTTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block5fixationTT" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block5fixationATT* *block5fixationBTT* updates
        if block5fixationATT.status == NOT_STARTED and block5fixationBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block5fixationATT.frameNStart = frameN  # exact frame index
            block5fixationATT.tStart = t  # local t and not account for scr refresh
            block5fixationATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block5fixationATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block5fixationATT.started')
            block5fixationATT.setAutoDraw(True)
            # keep track of start time/frame for later
            block5fixationBTT.frameNStart = frameNB  # exact frame index
            block5fixationBTT.tStart = tB  # local t and not account for scr refresh
            block5fixationBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block5fixationBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block5fixationBTT.started')
            block5fixationBTT.setAutoDraw(True)
        
        if block5fixationATT.status == STARTED and block5fixationBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block5fixationATT.tStartRefresh + jitter[0]-frameTolerance) and (tThisFlipGlobalB > block5fixationBTT.tStartRefresh + jitter[0]-frameTolerance):
                # keep track of stop time/frame for later
                block5fixationATT.tStop = t  # not accounting for scr refresh
                block5fixationATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block5fixationATT.stopped')
                block5fixationATT.setAutoDraw(False)
                # keep track of stop time/frame for later
                block5fixationBTT.tStop = tB  # not accounting for scr refresh
                block5fixationBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block5fixationBTT.stopped')
                block5fixationBTT.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block5fixationTTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block5fixationTT" ---
    for thisComponent in block5fixationTTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    # the Routine "block5fixationTT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block5imageTT" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    block5imageATT.setImage(imagesA5TT)
    block5key_respTT.keys = []
    block5key_respTT.rt = []
    _block5key_respTT_allKeys = []
    block5imageBTT.setImage(imagesB5TT)
    # keep track of which components have finished
    block5imageTTComponents = [p_port_block5imageATT, p_port_block5imageBTT, block5imageATT, block5key_respTT, block5imageBTT]
    for thisComponent in block5imageTTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block5imageTT" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_port_block5imageA* *p_port_block5imageB* updates
        if (p_port_block5imageATT.status == NOT_STARTED and block5imageATT.status == STARTED) and (p_port_block5imageBTT.status == NOT_STARTED and block5imageBTT.status == STARTED):
            # keep track of start time/frame for later
            p_port_block5imageATT.frameNStart = frameN  # exact frame index
            p_port_block5imageATT.tStart = t  # local t and not account for scr refresh
            p_port_block5imageATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_block5imageATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_port_block5imageATT.started')
            p_port_block5imageATT.status = STARTED
            win.callOnFlip(p_port_block5imageATT.setData, int(COA5TT))
    
            # keep track of start time/frame for later
            #serialport.frameNStart = frameNB  # exact frame index
            #serialport.tStart = tB  # local t and not account for scr refresh
            #serialport.tStartRefresh = tThisFlipGlobalB  # on global time
            #winB.timeOnFlip(serialport, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(winB, 'serialport.started')
            #serialport.status = STARTED
            #winB.callOnFlip(serialport.write, bytes('pracCOB', 'utf8'))
            
            p_port_block5imageBTT.frameNStart = frameNB  # exact frame index
            p_port_block5imageBTT.tStart = tB  # local t and not account for scr refresh
            p_port_block5imageBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(p_port_block5imageBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'p_port_block5imageBTT.started')
            p_port_block5imageBTT.status = STARTED
            winB.callOnFlip(p_port_block5imageBTT.setData, int(COB5TT))
            
            
        if p_port_block5imageATT.status == STARTED and p_port_block5imageBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > p_port_block5imageATT.tStartRefresh + 0.1-frameTolerance) and (tThisFlipGlobalB > p_port_block5imageBTT.tStartRefresh + 0.1-frameTolerance):
                # keep track of stop time/frame for later
                p_port_block5imageATT.tStop = t  # not accounting for scr refresh
                p_port_block5imageATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'p_port_block5imageATT.stopped')
                p_port_block5imageATT.status = FINISHED
                win.callOnFlip(p_port_block5imageATT.setData, int(0))
                
                # keep track of stop time/frame for later
                #serialport.tStop = tB  # not accounting for scr refresh
                #serialport.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(winB, 'serialport.stopped')
                #serialport.status = FINISHED
                #winB.callOnFlip(serialport.write, bytes('0', 'utf8'))
                
                # keep track of stop time/frame for later
                p_port_block5imageBTT.tStop = tB  # not accounting for scr refresh
                p_port_block5imageBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'p_port_block5imageBTT.stopped')
                p_port_block5imageBTT.status = FINISHED
                winB.callOnFlip(p_port_block5imageBTT.setData, int(0))
        
        # *block5imageATT* *block5imageBTT* updates
        if block5imageATT.status == NOT_STARTED and block5imageBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block5imageATT.frameNStart = frameN  # exact frame index
            block5imageATT.tStart = t  # local t and not account for scr refresh
            block5imageATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block5imageATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block5imageATT.started')
            block5imageATT.setAutoDraw(True)
            # keep track of start time/frame for later
            block5imageBTT.frameNStart = frameNB  # exact frame index
            block5imageBTT.tStart = tB  # local t and not account for scr refresh
            block5imageBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block5imageBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block5imageBTT.started')
            block5imageBTT.setAutoDraw(True)
            
        if block5imageATT.status == STARTED and block5imageBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block5imageATT.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block5imageBTT.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block5imageATT.tStop = t  # not accounting for scr refresh
                block5imageATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block5imageATT.stopped')
                block5imageATT.setAutoDraw(False)
                # keep track of stop time/frame for later
                block5imageBTT.tStop = tB  # not accounting for scr refresh
                block5imageBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block5imageBTT.stopped')
                block5imageBTT.setAutoDraw(False)
        
        # *block5key_respTT* updates
        waitOnFlip = False
        if block5key_respTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block5key_respTT.frameNStart = frameN  # exact frame index
            block5key_respTT.tStart = t  # local t and not account for scr refresh
            block5key_respTT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block5key_respTT, 'tStartRefresh')  # time at next scr refresh
            winB.timeOnFlip(block5key_respTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block5key_respTT.started')
            thisExp.timestampOnFlip(winB, 'block5key_respTTB.started')
            block5key_respTT.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block5key_respTT.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block5key_respTT.clearEvents, eventType='keyboard')  # clear events on next screen flip
            winB.callOnFlip(block5key_respTT.clock.reset)  # t=0 on next screen flip
            winB.callOnFlip(block5key_respTT.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block5key_respTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block5key_respTT.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                block5key_respTT.tStop = t  # not accounting for scr refresh
                block5key_respTT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block5key_respTT.stopped')
                thisExp.timestampOnFlip(winB, 'block5key_respTTB.stopped')
                block5key_respTT.status = FINISHED
        if block5key_respTT.status == STARTED and not waitOnFlip:
            theseKeys = block5key_respTT.getKeys(keyList=['num_1','num_3','num_7','num_9'], waitRelease=False)
            _block5key_respTT_allKeys.extend(theseKeys)
            if len(_block5key_respTT_allKeys):
                block5key_respTT.keys = [key.name for key in _block5key_respTT_allKeys]  # storing all keys
                block5key_respTT.rt = [key.rt for key in _block5key_respTT_allKeys]
                # was this correct?
                if (block5key_respTT.keys == str(correctkey5TT)) or (block5key_respTT.keys == correctkey5TT):
                    block5key_respTT.corr = 1
                else:
                    block5key_respTT.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block5imageTTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block5imageTT" ---
    for thisComponent in block5imageTTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    if p_port_block5imageATT.status == STARTED:
        win.callOnFlip(p_port_block5imageATT.setData, int(0))
    if p_port_block5imageBTT.status == STARTED:
        winB.callOnFlip(p_port_block5imageBTT.setData, int(0))
    # check responses
    if block5key_respTT.keys in ['', [], None]:  # No response was made
        block5key_respTT.keys = None
        # was no response the correct answer?!
        if str(correctkey5TT).lower() == 'none':
           block5key_respTT.corr = 1;  # correct non-response
        else:
           block5key_respTT.corr = 0;  # failed to respond (incorrectly)
    # store data for block5TT (TrialHandler)
    block5TT.addData('block5key_respTT.keys',block5key_respTT.keys)
    block5TT.addData('block5key_respTT.corr', block5key_respTT.corr)
    if block5key_respTT.keys != None:  # we had a response
        block5TT.addData('block5key_respTT.rt', block5key_respTT.rt)
    # the Routine "block5imageTT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block5TT'


# --- Prepare to start Routine "block6instruction" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
# keep track of which components have finished
block6instructionComponents = [block6TextA, block6TextB]
for thisComponent in block6instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "block6instruction" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block6TextA* *block6TextB* updates
    if block6TextA.status == NOT_STARTED and block6TextB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block6TextA.frameNStart = frameN  # exact frame index
        block6TextA.tStart = t  # local t and not account for scr refresh
        block6TextA.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block6TextA, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'block6TextA.started')
        block6TextA.setAutoDraw(True)
        # keep track of start time/frame for later
        block6TextB.frameNStart = frameNB  # exact frame index
        block6TextB.tStart = tB  # local t and not account for scr refresh
        block6TextB.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(block6TextB, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'block6TextB.started')
        block6TextB.setAutoDraw(True)
        
    if block6TextA.status == STARTED and block6TextB.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if (tThisFlipGlobal > block6TextA.tStartRefresh + 10-frameTolerance) and (tThisFlipGlobalB > block6TextB.tStartRefresh + 10-frameTolerance):
            # keep track of stop time/frame for later
            block6TextA.tStop = t  # not accounting for scr refresh
            block6TextA.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block6TextA.stopped')
            block6TextA.setAutoDraw(False)
             # keep track of stop time/frame for later
            block6TextB.tStop = tB  # not accounting for scr refresh
            block6TextB.frameNStop = frameNB  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block6TextB.stopped')
            block6TextB.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block6instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "block6instruction" ---
for thisComponent in block6instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
block6 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('group1_b6.xlsx'),
    seed=None, name='block6')
thisExp.addLoop(block6)  # add the loop to the experiment
thisBlock6 = block6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock6.rgb)
if thisBlock6 != None:
    for paramName in thisBlock6:
        exec('{} = thisBlock6[paramName]'.format(paramName))

for thisBlock6 in block6:
    currentLoop = block6
    # abbreviate parameter names if possible (e.g. rgb = thisBlock6.rgb)
    if thisBlock6 != None:
        for paramName in thisBlock6:
            exec('{} = thisBlock6[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block6fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code6
    jitter = np.arange(1, 1.2, .10)
    shuffle(jitter)
    block6fixationA.setText('+')
    block6fixationB.setText('+')
    # keep track of which components have finished
    block6fixationComponents = [block6fixationA, block6fixationB]
    for thisComponent in block6fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block6fixation" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block6fixationA* *block6fixationB* updates
        if block6fixationA.status == NOT_STARTED and block6fixationB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block6fixationA.frameNStart = frameN  # exact frame index
            block6fixationA.tStart = t  # local t and not account for scr refresh
            block6fixationA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block6fixationA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block6fixationA.started')
            block6fixationA.setAutoDraw(True)
            # keep track of start time/frame for later
            block6fixationB.frameNStart = frameNB  # exact frame index
            block6fixationB.tStart = tB  # local t and not account for scr refresh
            block6fixationB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block6fixationB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block6fixationB.started')
            block6fixationB.setAutoDraw(True)
        if block6fixationA.status == STARTED and block6fixationB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block6fixationA.tStartRefresh + jitter[0]-frameTolerance) and (tThisFlipGlobalB > block6fixationB.tStartRefresh + jitter[0]-frameTolerance):
                # keep track of stop time/frame for later
                block6fixationA.tStop = t  # not accounting for scr refresh
                block6fixationA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block6fixationA.stopped')
                block6fixationA.setAutoDraw(False)
                # keep track of stop time/frame for later
                block6fixationB.tStop = tB  # not accounting for scr refresh
                block6fixationB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block6fixationB.stopped')
                block6fixationB.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block6fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block6fixation" ---
    for thisComponent in block6fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    # the Routine "block6fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block6image" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    block6borderA.setImage(frameA6)
    block6imageA.setImage(imagesA6)
    block6key_resp.keys = []
    block6key_resp.rt = []
    _block6key_resp_allKeys = []
    block6borderB.setImage(frameB6)
    block6imageB.setImage(imagesB6)
    # keep track of which components have finished
    block6imageComponents = [p_port_block6imageA, p_port_block6imageB, block6borderA, block6imageA, block6key_resp, block6borderB, block6imageB]
    for thisComponent in block6imageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block6image" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_port_block6imageA* *p_port_block6imageB* updates
        if (p_port_block6imageA.status == NOT_STARTED and block6imageA.status == STARTED) and (p_port_block6imageB.status == NOT_STARTED and block6imageB.status == STARTED):
            # keep track of start time/frame for later
            p_port_block6imageA.frameNStart = frameN  # exact frame index
            p_port_block6imageA.tStart = t  # local t and not account for scr refresh
            p_port_block6imageA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_block6imageA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_port_block6imageA.started')
            p_port_block6imageA.status = STARTED
            win.callOnFlip(p_port_block6imageA.setData, int(COA6))
    
            # keep track of start time/frame for later
            #serialport.frameNStart = frameNB  # exact frame index
            #serialport.tStart = tB  # local t and not account for scr refresh
            #serialport.tStartRefresh = tThisFlipGlobalB  # on global time
            #winB.timeOnFlip(serialport, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(winB, 'serialport.started')
            #serialport.status = STARTED
            #winB.callOnFlip(serialport.write, bytes('pracCOB', 'utf8'))
            
            p_port_block6imageB.frameNStart = frameNB  # exact frame index
            p_port_block6imageB.tStart = tB  # local t and not account for scr refresh
            p_port_block6imageB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(p_port_block6imageB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'p_port_block6imageB.started')
            p_port_block6imageB.status = STARTED
            winB.callOnFlip(p_port_block6imageB.setData, int(COB6))
            
            
        if p_port_block6imageA.status == STARTED and p_port_block6imageB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > p_port_block6imageA.tStartRefresh + 0.1-frameTolerance) and (tThisFlipGlobalB > p_port_block6imageB.tStartRefresh + 0.1-frameTolerance):
                # keep track of stop time/frame for later
                p_port_block6imageA.tStop = t  # not accounting for scr refresh
                p_port_block6imageA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'p_port_block6imageA.stopped')
                p_port_block6imageA.status = FINISHED
                win.callOnFlip(p_port_block6imageA.setData, int(0))
                
                # keep track of stop time/frame for later
                #serialport.tStop = tB  # not accounting for scr refresh
                #serialport.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(winB, 'serialport.stopped')
                #serialport.status = FINISHED
                #winB.callOnFlip(serialport.write, bytes('0', 'utf8'))
                
                # keep track of stop time/frame for later
                p_port_block6imageB.tStop = tB  # not accounting for scr refresh
                p_port_block6imageB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'p_port_block6imageB.stopped')
                p_port_block6imageB.status = FINISHED
                winB.callOnFlip(p_port_block6imageB.setData, int(0))
        
        # *block6borderA* *block6borderB* updates
        if block6borderA.status == NOT_STARTED and block6borderB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block6borderA.frameNStart = frameN  # exact frame index
            block6borderA.tStart = t  # local t and not account for scr refresh
            block6borderA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block6borderA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block6borderA.started')
            block6borderA.setAutoDraw(True)
            # keep track of start time/frame for later
            block6borderB.frameNStart = frameNB  # exact frame index
            block6borderB.tStart = tB  # local t and not account for scr refresh
            block6borderB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block6borderB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block6borderB.started')
            block6borderB.setAutoDraw(True)
            
        if block6borderA.status == STARTED and block6borderB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block6borderA.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block6borderB.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block6borderA.tStop = t  # not accounting for scr refresh
                block6borderA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block6borderA.stopped')
                block6borderA.setAutoDraw(False)
                # keep track of stop time/frame for later
                block6borderB.tStop = tB  # not accounting for scr refresh
                block6borderB.frameNStop = frameNB # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block6borderB.stopped')
                block6borderB.setAutoDraw(False)
        
        # *block6imageA* *block6imageB* updates
        if block6imageA.status == NOT_STARTED and block6imageB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block6imageA.frameNStart = frameN  # exact frame index
            block6imageA.tStart = t  # local t and not account for scr refresh
            block6imageA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block6imageA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block6imageA.started')
            block6imageA.setAutoDraw(True)
            # keep track of start time/frame for later
            block6imageB.frameNStart = frameNB  # exact frame index
            block6imageB.tStart = tB  # local t and not account for scr refresh
            block6imageB.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block6imageB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block6imageB.started')
            block6imageB.setAutoDraw(True)
            
        if block6imageA.status == STARTED and block6imageB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block6imageA.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block6imageB.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block6imageA.tStop = t  # not accounting for scr refresh
                block6imageA.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block6imageA.stopped')
                block6imageA.setAutoDraw(False)
                 # keep track of stop time/frame for later
                block6imageB.tStop = tB  # not accounting for scr refresh
                block6imageB.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block6imageB.stopped')
                block6imageB.setAutoDraw(False)
        
        # *block6key_resp* updates
        waitOnFlip = False
        if block6key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block6key_resp.frameNStart = frameN  # exact frame index
            block6key_resp.tStart = t  # local t and not account for scr refresh
            block6key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block6key_resp, 'tStartRefresh')  # time at next scr refresh
            winB.timeOnFlip(block6key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block6key_resp.started')
            thisExp.timestampOnFlip(winB, 'block6key_respB.started')
            block6key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block6key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block6key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            winB.callOnFlip(block6key_resp.clock.reset)  # t=0 on next screen flip
            winB.callOnFlip(block6key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block6key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block6key_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                block6key_resp.tStop = t  # not accounting for scr refresh
                block6key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block6key_resp.stopped')
                thisExp.timestampOnFlip(winB, 'block6key_respB.stopped')
                block6key_resp.status = FINISHED
        if block6key_resp.status == STARTED and not waitOnFlip:
            theseKeys = block6key_resp.getKeys(keyList=['num_1','num_3','num_7','num_9'], waitRelease=False)
            _block6key_resp_allKeys.extend(theseKeys)
            if len(_block6key_resp_allKeys):
                block6key_resp.keys = [key.name for key in _block6key_resp_allKeys]  # storing all keys
                block6key_resp.rt = [key.rt for key in _block6key_resp_allKeys]
                # was this correct?
                if (block6key_resp.keys == str(correctkey6)) or (prac_key_resp.keys == correctkey6):
                    block6key_resp.corr = 1
                else:
                    block6key_resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block6imageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block6image" ---
    for thisComponent in block6imageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    if p_port_block6imageA.status == STARTED:
        win.callOnFlip(p_port_block6imageA.setData, int(0))
    if p_port_block6imageB.status == STARTED:
        winB.callOnFlip(p_port_block6imageB.setData, int(0))
    # check responses
    if block6key_resp.keys in ['', [], None]:  # No response was made
        block6key_resp.keys = None
        # was no response the correct answer?!
        if str(correctkey6).lower() == 'none':
           block6key_resp.corr = 1;  # correct non-response
        else:
           block6key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for block6 (TrialHandler)
    block6.addData('block6key_resp.keys',block6key_resp.keys)
    block6.addData('block6key_resp.corr', block6key_resp.corr)
    if block6key_resp.keys != None:  # we had a response
        block6.addData('block6key_resp.rt', block6key_resp.rt)
    # the Routine "block6image" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block6'


# --- Prepare to start Routine "block6instructionTT" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
# keep track of which components have finished
block6instructionTTComponents = [block6TextATT, block6TextBTT]
for thisComponent in block6instructionTTComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "block6instructionTT" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block6TextATT* *block6TextBTT* updates
    if block6TextATT.status == NOT_STARTED and block6TextBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block6TextATT.frameNStart = frameN  # exact frame index
        block6TextATT.tStart = t  # local t and not account for scr refresh
        block6TextATT.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block6TextATT, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'block6TextATT.started')
        block6TextATT.setAutoDraw(True)
        # keep track of start time/frame for later
        block6TextBTT.frameNStart = frameNB  # exact frame index
        block6TextBTT.tStart = tB  # local t and not account for scr refresh
        block6TextBTT.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(block6TextBTT, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'block6TextBTT.started')
        block6TextBTT.setAutoDraw(True)
        
    if block6TextATT.status == STARTED and block6TextBTT.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if (tThisFlipGlobal > block6TextATT.tStartRefresh + 10-frameTolerance) and (tThisFlipGlobalB > block6TextBTT.tStartRefresh + 10-frameTolerance):
            # keep track of stop time/frame for later
            block6TextATT.tStop = t  # not accounting for scr refresh
            block6TextATT.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block6TextATT.stopped')
            block6TextATT.setAutoDraw(False)
            # keep track of stop time/frame for later
            block6TextBTT.tStop = tB  # not accounting for scr refresh
            block6TextBTT.frameNStop = frameNB  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block6TextBTT.stopped')
            block6TextBTT.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block6instructionTTComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "block6instructionTT" ---
for thisComponent in block6instructionTTComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
block6TT = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('group1_b6TT.xlsx'),
    seed=None, name='block6TT')
thisExp.addLoop(block6TT)  # add the loop to the experiment
thisBlock6TT = block6TT.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock6TT.rgb)
if thisBlock6TT != None:
    for paramName in thisBlock6TT:
        exec('{} = thisBlock6TT[paramName]'.format(paramName))

for thisBlock6TT in block6TT:
    currentLoop = block6TT
    # abbreviate parameter names if possible (e.g. rgb = thisBlock6TT.rgb)
    if thisBlock6TT != None:
        for paramName in thisBlock6TT:
            exec('{} = thisBlock6TT[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block6fixationTT" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code6TT
    jitter = np.arange(1, 1.2, .10)
    shuffle(jitter)
    block6fixationATT.setText('+')
    block6fixationBTT.setText('+')
    # keep track of which components have finished
    block6fixationTTComponents = [block6fixationATT, block6fixationBTT]
    for thisComponent in block6fixationTTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block6fixationTT" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block6fixationATT* *block6fixationBTT* updates
        if block6fixationATT.status == NOT_STARTED and block6fixationBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block6fixationATT.frameNStart = frameN  # exact frame index
            block6fixationATT.tStart = t  # local t and not account for scr refresh
            block6fixationATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block6fixationATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block6fixationATT.started')
            block6fixationATT.setAutoDraw(True)
            # keep track of start time/frame for later
            block6fixationBTT.frameNStart = frameNB  # exact frame index
            block6fixationBTT.tStart = tB  # local t and not account for scr refresh
            block6fixationBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block6fixationBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block6fixationBTT.started')
            block6fixationBTT.setAutoDraw(True)
        
        if block6fixationATT.status == STARTED and block6fixationBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block6fixationATT.tStartRefresh + jitter[0]-frameTolerance) and (tThisFlipGlobalB > block6fixationBTT.tStartRefresh + jitter[0]-frameTolerance):
                # keep track of stop time/frame for later
                block6fixationATT.tStop = t  # not accounting for scr refresh
                block6fixationATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block6fixationATT.stopped')
                block6fixationATT.setAutoDraw(False)
                # keep track of stop time/frame for later
                block6fixationBTT.tStop = tB  # not accounting for scr refresh
                block6fixationBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block6fixationBTT.stopped')
                block6fixationBTT.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block6fixationTTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block6fixationTT" ---
    for thisComponent in block6fixationTTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    # the Routine "block6fixationTT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block6imageTT" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code
    win.mouseVisible = True
    winB.mouseVisible = True
    # update component parameters for each repeat
    block6imageATT.setImage(imagesA6TT)
    block6key_respTT.keys = []
    block6key_respTT.rt = []
    _block6key_respTT_allKeys = []
    block6imageBTT.setImage(imagesB6TT)
    # keep track of which components have finished
    block6imageTTComponents = [p_port_block6imageATT, p_port_block6imageBTT, block6imageATT, block6key_respTT, block6imageBTT]
    for thisComponent in block6imageTTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    tB = 0
    _timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
    frameNB = -1
    
    # --- Run Routine "block6imageTT" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        tB = routineTimer.getTime()
        tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
        frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_port_block6imageA* *p_port_block6imageB* updates
        if (p_port_block6imageATT.status == NOT_STARTED and block6imageATT.status == STARTED) and (p_port_block6imageBTT.status == NOT_STARTED and block6imageBTT.status == STARTED):
            # keep track of start time/frame for later
            p_port_block6imageATT.frameNStart = frameN  # exact frame index
            p_port_block6imageATT.tStart = t  # local t and not account for scr refresh
            p_port_block6imageATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_block6imageATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_port_block6imageATT.started')
            p_port_block6imageATT.status = STARTED
            win.callOnFlip(p_port_block6imageATT.setData, int(COA6TT))
    
            # keep track of start time/frame for later
            #serialport.frameNStart = frameNB  # exact frame index
            #serialport.tStart = tB  # local t and not account for scr refresh
            #serialport.tStartRefresh = tThisFlipGlobalB  # on global time
            #winB.timeOnFlip(serialport, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(winB, 'serialport.started')
            #serialport.status = STARTED
            #winB.callOnFlip(serialport.write, bytes('pracCOB', 'utf8'))
            
            p_port_block6imageBTT.frameNStart = frameNB  # exact frame index
            p_port_block6imageBTT.tStart = tB  # local t and not account for scr refresh
            p_port_block6imageBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(p_port_block6imageBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'p_port_block6imageBTT.started')
            p_port_block6imageBTT.status = STARTED
            winB.callOnFlip(p_port_block6imageBTT.setData, int(COB6TT))
            
            
        if p_port_block6imageATT.status == STARTED and p_port_block6imageBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > p_port_block6imageATT.tStartRefresh + 0.1-frameTolerance) and (tThisFlipGlobalB > p_port_block6imageBTT.tStartRefresh + 0.1-frameTolerance):
                # keep track of stop time/frame for later
                p_port_block6imageATT.tStop = t  # not accounting for scr refresh
                p_port_block6imageATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'p_port_block6imageATT.stopped')
                p_port_block6imageATT.status = FINISHED
                win.callOnFlip(p_port_block6imageATT.setData, int(0))
                
                # keep track of stop time/frame for later
                #serialport.tStop = tB  # not accounting for scr refresh
                #serialport.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(winB, 'serialport.stopped')
                #serialport.status = FINISHED
                #winB.callOnFlip(serialport.write, bytes('0', 'utf8'))
                
                # keep track of stop time/frame for later
                p_port_block6imageBTT.tStop = tB  # not accounting for scr refresh
                p_port_block6imageBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'p_port_block6imageBTT.stopped')
                p_port_block6imageBTT.status = FINISHED
                winB.callOnFlip(p_port_block6imageBTT.setData, int(0))
        
        # *block6imageATT* *block6imageBTT* updates
        if block6imageATT.status == NOT_STARTED and block6imageBTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block6imageATT.frameNStart = frameN  # exact frame index
            block6imageATT.tStart = t  # local t and not account for scr refresh
            block6imageATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block6imageATT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block6imageATT.started')
            block6imageATT.setAutoDraw(True)
            # keep track of start time/frame for later
            block6imageBTT.frameNStart = frameNB  # exact frame index
            block6imageBTT.tStart = tB  # local t and not account for scr refresh
            block6imageBTT.tStartRefresh = tThisFlipGlobalB  # on global time
            winB.timeOnFlip(block6imageBTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(winB, 'block6imageBTT.started')
            block6imageBTT.setAutoDraw(True)
            
        if block6imageATT.status == STARTED and block6imageBTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if (tThisFlipGlobal > block6imageATT.tStartRefresh + 2-frameTolerance) and (tThisFlipGlobalB > block6imageBTT.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                block6imageATT.tStop = t  # not accounting for scr refresh
                block6imageATT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block6imageATT.stopped')
                block6imageATT.setAutoDraw(False)
                # keep track of stop time/frame for later
                block6imageBTT.tStop = tB  # not accounting for scr refresh
                block6imageBTT.frameNStop = frameNB  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(winB, 'block6imageBTT.stopped')
                block6imageBTT.setAutoDraw(False)
        
        # *block6key_respTT* updates
        waitOnFlip = False
        if block6key_respTT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block6key_respTT.frameNStart = frameN  # exact frame index
            block6key_respTT.tStart = t  # local t and not account for scr refresh
            block6key_respTT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block6key_respTT, 'tStartRefresh')  # time at next scr refresh
            winB.timeOnFlip(block6key_respTT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block6key_respTT.started')
            thisExp.timestampOnFlip(winB, 'block6key_respTTB.started')
            block6key_respTT.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block6key_respTT.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block6key_respTT.clearEvents, eventType='keyboard')  # clear events on next screen flip
            winB.callOnFlip(block6key_respTT.clock.reset)  # t=0 on next screen flip
            winB.callOnFlip(block6key_respTT.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block6key_respTT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block6key_respTT.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                block6key_respTT.tStop = t  # not accounting for scr refresh
                block6key_respTT.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block6key_respTT.stopped')
                thisExp.timestampOnFlip(winB, 'block6key_respTTB.stopped')
                block6key_respTT.status = FINISHED
        if block6key_respTT.status == STARTED and not waitOnFlip:
            theseKeys = block6key_respTT.getKeys(keyList=['num_1','num_3','num_7','num_9'], waitRelease=False)
            _block6key_respTT_allKeys.extend(theseKeys)
            if len(_block6key_respTT_allKeys):
                block6key_respTT.keys = [key.name for key in _block6key_respTT_allKeys]  # storing all keys
                block6key_respTT.rt = [key.rt for key in _block6key_respTT_allKeys]
                # was this correct?
                if (block6key_respTT.keys == str(correctkey6TT)) or (block6key_respTT.keys == correctkey6TT):
                    block6key_respTT.corr = 1
                else:
                    block6key_respTT.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block6imageTTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            winB.flip()
    
    # --- Ending Routine "block6imageTT" ---
    for thisComponent in block6imageTTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.mouseVisible = False
    winB.mouseVisible = False
    if p_port_block6imageATT.status == STARTED:
        win.callOnFlip(p_port_block6imageATT.setData, int(0))
    if p_port_block6imageBTT.status == STARTED:
        winB.callOnFlip(p_port_block6imageBTT.setData, int(0))
    # check responses
    if block6key_respTT.keys in ['', [], None]:  # No response was made
        block6key_respTT.keys = None
        # was no response the correct answer?!
        if str(correctkey6TT).lower() == 'none':
           block6key_respTT.corr = 1;  # correct non-response
        else:
           block6key_respTT.corr = 0;  # failed to respond (incorrectly)
    # store data for block6TT (TrialHandler)
    block6TT.addData('block6key_respTT.keys',block6key_respTT.keys)
    block6TT.addData('block6key_respTT.corr', block6key_respTT.corr)
    if block6key_respTT.keys != None:  # we had a response
        block6TT.addData('block6key_respTT.rt', block6key_respTT.rt)
    # the Routine "block6imageTT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block6TT'


# --- Prepare to start Routine "endmessage" ---
continueRoutine = True
routineForceEnded = False
# Run 'Begin Routine' code from code
win.mouseVisible = True
winB.mouseVisible = True
# update component parameters for each repeat
SPACE_3.keys = []
SPACE_3.rt = []
_SPACE_3_allKeys = []
# keep track of which components have finished
endmessageComponents = [endTextA, endTextB, SPACE_3]
for thisComponent in endmessageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

tB = 0
_timeToFirstFrameB = winB.getFutureFlipTime(clock="now")
frameNB = -1

# --- Run Routine "endmessage" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    tB = routineTimer.getTime()
    tThisFlipB = winB.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobalB = winB.getFutureFlipTime(clock=None)
    frameNB = frameNB + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endTextA* *endTextB* updates
    if endTextA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance and endTextB.status == NOT_STARTED:
        # keep track of start time/frame for later
        endTextA.frameNStart = frameN  # exact frame index
        endTextA.tStart = t  # local t and not account for scr refresh
        endTextA.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endTextA, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endTextA.started')
        endTextA.setAutoDraw(True)
        # keep track of start time/frame for later
        endTextB.frameNStart = frameNB  # exact frame index
        endTextB.tStart = tB  # local t and not account for scr refresh
        endTextB.tStartRefresh = tThisFlipGlobalB  # on global time
        winB.timeOnFlip(endTextB, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(winB, 'endTextB.started')
        endTextB.setAutoDraw(True)
    
    # *SPACE_3* updates
    waitOnFlip = False
    if SPACE_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SPACE_3.frameNStart = frameN  # exact frame index
        SPACE_3.tStart = t  # local t and not account for scr refresh
        SPACE_3.tStartRefresh = tThisFlipGlobal  # on global time
        SPACE_3.frameNStart = frameNB  # exact frame index
        SPACE_3.tStart = tB  # local t and not account for scr refresh
        SPACE_3.tStartRefresh = tThisFlipGlobalB  # on global time
        win.timeOnFlip(SPACE_3, 'tStartRefresh')  # time at next scr refresh
        winB.timeOnFlip(SPACE_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'SPACE_3.started')
        thisExp.timestampOnFlip(winB, 'SPACE_3B.started')
        SPACE_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(SPACE_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(SPACE_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        winB.callOnFlip(SPACE_3.clock.reset)  # t=0 on next screen flip
        winB.callOnFlip(SPACE_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if SPACE_3.status == STARTED and not waitOnFlip:
        theseKeys = SPACE_3.getKeys(keyList=['space'], waitRelease=False)
        _SPACE_3_allKeys.extend(theseKeys)
        if len(_SPACE_3_allKeys):
            SPACE_3.keys = _SPACE_3_allKeys[-1].name  # just the last key pressed
            SPACE_3.rt = _SPACE_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endmessageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        winB.flip()

# --- Ending Routine "endmessage" ---
for thisComponent in endmessageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.mouseVisible = False
winB.mouseVisible = False
# check responses
if SPACE_3.keys in ['', [], None]:  # No response was made
    SPACE_3.keys = None
thisExp.addData('SPACE_3.keys',SPACE_3.keys)
if SPACE_3.keys != None:  # we had a response
    thisExp.addData('SPACE_3.rt', SPACE_3.rt)
thisExp.nextEntry()
# the Routine "endmessage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# Close serialPort
if serialport.is_open:
    serialport.close()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()
winB.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

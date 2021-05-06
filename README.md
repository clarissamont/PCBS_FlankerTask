# Flanker Task
### *Effects of noise letters upon the identification of a target letter in a nonsearch task (Eriksen & Eriksen, 1974)*

## Original Experiment Description: 

The main goal of the original study was to observe response inhibition - that is, our ability to suppress responses that are contextually inappropriate given the task at hand. We provoke this response by presenting target stimuli with noise that provides either relevant or irrelevant information (i.e. "flankers"). 

The task consists of three types of stimuli, differing in how the flankers relate to the target stimulus. 

The target stimuli are arbitrarily chosen letters, assigned to directional responses (e.g. H & K = right; S & C = left). They are presented in the midst of flanker letters which surround them. Participants are instructed to press a button (right or left) depending on the directional association of the target stimulus (which is always in the middle of the letters presented in the stimulus. 

In **congruent stimuli** the target letter and the flankers correspond to the same directional response (e.g. HHHKHHH), in **incongruent stimuli**, the target letter and the flankers correspond to opposing directional responses (e.g. SSSKSSS), and in **neutral stimuli**, the flankers are letters which have not been assigned a directional response (e.g. NWZKNWZ). 

In the original study, participant responses were slower and less accurate in the incongruent condition, indicating difficulties inibiting responses that have been influenced by irrelevant noise. 

## PCBS Project Description: 

In this rendition of the Eriksen Flanker task, I have simplified the original letter-based task by using left- and right-pointing arrows (i.e. "<" and ">") as stimuli. The premise of the experiment is identical to the original task with letters associated to direction; that is, the participant is required to fixate on a cross in the middle of the screen, prior to seeing stimuli where the arrows surrounding the middle arrow are either **congruent** ("<<<<<", ">>>>>"), **neutral** ("||<||", ||>||")* or **incongruent** ("<<><<", ">><>>") with the arrow in the middle position. The only difference is that here, the participant no longer needs to create the association between letter and direction.

The participant's task is to indicate whether the center arrow is pointing to the left or the right by pressing the right or left arrows on the keyboard, respectively.

The task is expected to be the most difficult for participants when doing the congruent task; that is, they will probably have slower reaction times and less accurate responses overall.

\* *I created the "neutral" stimuli in an attempt to replicate the "neutral" condition of the original experiment. I tried to choose a symbol that would not bias perception of arrow direction, but that would just be added noise. This is why I chose the "|" symbol.*

## Running This Experiment:

To execute this experiment, please download and run "flanker.py" on python. After the experiment ends (it will do so automatically), the participant data should be saved to the same folder where you downlaoded the "flanker.py" file. 

The data will be labelled flanker_ParticipantNumber_Date.xpd. In this file, you will find: the subject ID, block of the experiment (1-6), correct response for each trial (275 = RIGHT, 276 = LEFT), participant response for each trial (275 = RIGHT, 276 = LEFT), trial number (between 0 and 5 for each block), response time, response accuracy (1 = correct, 0 = incorrect), and trial type (congruent, neutral, or incongruent). 

An example of a .xpd file with sample data can be found at: https://github.com/clarissamont/PCBS_FlankerTask/blob/main/flanker_00_202105051412.xpd

## Previous Coding Experience & PCBS Comments: 

I don't have very much coding experience. In my undergrad I did a little bit of data analysis/statistics using R, but I have only been learning Python since the beginning of the Cogmaster (i.e. the datacamp class in S1). 

I liked this course because it pushed me to apply things I learned about Python in the first semester. The lectures early on in the course were great as reminders/ learning useful skills that I should know. It's also very useful to know how to design experiments using expyriment!

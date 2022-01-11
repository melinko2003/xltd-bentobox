#!/usr/bin/python3

# bentobox-cli 
# Uses the Bento Library to create, manipulate, remove Bentobox Projects.

import sys, argparse
# import bentobox

app_name='bentobox'

# Parser Arguements
parser = argparse.ArgumentParser(description='Help Construct Messages')

# Mode Selection w/ Crud(a) Generics
parser.add_argument('-m', '--mode', choices=['create', 'read', 'update', 'delete', 'adv'], required=True, help="Options that are available are 'create', 'read', 'update', 'delete', 'adv' ")
# Destination to a Project
parser.add_argument('-d', '--dest', type=str, required=False, help='Path to new ' + app_name + ' project')
# Path to an Existing Project
parser.add_argument('-s', '--src', type=str, required=False, help='Path of existing ' + app_name + ' project')
# Naming the Project
parser.add_argument('-n', '--name', type=str, required=False, help='Name your ' + app_name + ' project')
# Features included in the project ( See Supported Types: ToDo .. Tenative: cli, flask, apache-flask, web-gui, api, restful-api, soap-api)
parser.add_argument('-f', '--feat', type=str, required=False, help='Provide a comma seperated List of the features you wish to include in your ' + app_name + ' project')
# Use a provisioning file, which this CLI actually does w/some guessing and then executes it, this is just a short cut.
parser.add_argument('-p', '--provision', type=str, required=False, help='Path to ' + app_name + ' provisioing yaml file')
# Clone an Existing Project.
parser.add_argument('-c', '--clone', type=str, required=False, help='Clone one of your existing ' + app_name + ' projects')

try:
    bentobox.cli(params=parser.parse_args())
except:
    parser.print_help()
    sys.exit(0)



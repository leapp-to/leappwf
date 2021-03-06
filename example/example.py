#!/usr/bin/env python
""" Build and run workflow using LeApp Workflow module """

import leappwf

if __name__ == '__main__':
    wf = leappwf.LeAppWorkflow('./actors')
    wf.load_actors()
    ret = wf.run_actors()
    for actor, data in ret.items():
        print("* {}:".format(actor))
        print("[retcode]: {}".format(data['retcode']))
        if data['error']:
            print("\t[error]: {}".format(data['error']))

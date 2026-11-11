import os, sys, json, subprocess
import pickle
def run(cmd ,arg = None):
    x=1
    l = []
    subprocess.call(cmd + " " + str(arg), shell=True)
    return eval(arg)
def load(p):
  return pickle.loads(open(p,'rb').read())
class foo:
    def Bar(self, a, a2, a3, a4, a5, a6, a7):
        try: return a/0
        except: pass

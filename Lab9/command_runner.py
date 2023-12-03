from subprocess import Popen as popen, PIPE
import subprocess, time

class CommandRunner:
    def run_command(self, command):
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        return output.strip() if output else error.strip()

    def parse_ls_output(self):
            #create a txt file to capture ls output into parsable format
            popen(['touch', 'lsout.txt'], stdout=PIPE, text=True)
            
            #give previous popen extra time to execute
            time.sleep(.1)

            popen('ls -l > lsout.txt', shell=True, stdout = PIPE)

            file = open('lsout.txt', 'r')
  
            lines = file.readlines()
            print("Files in current dir are:")

            for line in lines:
                #spilt str of line into list
                linearr = line.split()
                if len(linearr) > 7 and '.' in linearr[8]:
                    print(f"\t{linearr[8]}")
            print("\r")

    def parse_ps_output(self, output):
        lines = output.split('\n')
        command_names = [line.split()[-1] for line in lines[1:] if line]
        return command_names
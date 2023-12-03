from command_runner import CommandRunner
import os

if __name__ == "__main__":
    # Instantiate CommandRunner
    cmd_runner = CommandRunner()

    #set working directory to current directory of script at runtime
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    cmd_runner.run_command("ls -l")

    cmd_runner.parse_ls_output()

    # Test ps aux command
    ps_output = cmd_runner.run_command('ps aux')
    print("\nps aux Output:")
    print(ps_output)

    # Test parse_ps_output method
    print("\nParsed ps aux Output:")
    print(cmd_runner.parse_ps_output(ps_output))
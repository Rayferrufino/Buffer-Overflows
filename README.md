# Buffer-Overflows
Diving into stack and head memory corruption

# Performing a BO - Verify
1. **Run vulnerable application and attach it to Immunity Debugger**
2. **Ensure you have a script that can normally communicate target protocol**
3. **Perform Fuzzing on that script with a single character until application crashes**
1. **Figure out which registers contain memory addresses that are overridden**
2. **Figure out which registers are overridden themselves (this is only good ifit’s EIP)**
4. **Locate the bytes at which EIP was overridden**

# Performing a BO - Execute

1. **Ensure you have enough room to hide a payload that is your reverse shell ( 350 bytes would be perfect!)**
2. **Determine bad characters**
3. **Work on redirection, need to find DLL. Use mona!**
4. **Make sure you look for at least 4 falses (first 4, hopefully 5)**
5. **Generate payload and update your exploit code**
6. **Exploit!**

# Why JMP ESP?

**ESP points directly to the start of your payload (after execution of the ret in the function you're attacking) because you put the payload right after the 4 bytes that overwrite the return address on the stack. ret pops 4 (or 8) bytes into EIP, leaving ESP pointing to the payload that directly follows.**

## Overall Steps:
- #### Fuzz (Crash a Program)
- #### Control EIP
    - Pattern_create / Pattern_offset
    - In mona.py or in msf (.rb)
- #### Locate Space for your Shellcode
    - Standard Shellcode requires 350-400 Bytes
    - Stagers requires
- #### Determine Bad Characters
    - Need to do multiple times (breaks on bad characters)
    - Stop when see FE, FF (or end non-bad chars)
- #### Redirect Program Execution
    - Locate modules without protections
    - !mona modules
    - Find a return address (JMP ESP)
    - Does not have to be a single instruction
- #### Generate appropriate shellcode
    - Must match OS version (32/64)
    - Different prompts based on shellcode type
    - EXITFUNC = Thread
    - -e (specify encoder)
- #### Get a Shell
    - Different prompts
    - Sometimes blank (no leading symbol)

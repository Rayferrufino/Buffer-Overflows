# Buffer-Overflows
Diving into stack and head memory corruption

# Performing a BO - Verify
1. **Run vulnerable application and attach it to Immunity Debugger
2. **Ensure you have a script that can normally communicate target protocol
3. **Perform Fuzzing on that script with a single character until application
crashes
1. **Figure out which registers contain memory addresses that are overridden.
2. **Figure out which registers are overridden themselves (this is only good if
it’s EIP).
4. **Locate the bytes at which EIP was overridden.

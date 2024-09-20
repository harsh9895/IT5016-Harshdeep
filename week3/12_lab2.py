"""
Converts a wavelength in nanometers to its corresponding color.
Parameters: wave_length (int): The wavelength in nanometers.
Returns:str: The color corresponding to the wavelength.
"""
def wavelength_to_color(wave_length):
   if wave_length > 750:
      return "The wavelength entered is higher than the visible spectrum! This is infrared."
   elif wave_length >= 620:
      return "Red"
   elif wave_length >= 590:
     return "Orange"
   elif wave_length >= 570:
     return "Yellow"
   elif wave_length >= 495:
     return "Green"
   elif wave_length >= 450:
     return "Blue"
   elif wave_length >= 380:
     return "Violet"
   else:
     return "Indeterminate, :-(, the number entered is outside the visible spectrum!" 
   
# Main execution
print(f"Welcome to wavelength to colour converter\n")
wave_length = int(input(f"Please enter an integer wavelength between 380 and 750>>"))
print(f"Thank you, the wavelength that you entered in nanometres is:{wave_length} \n")
print(f"The colour for this wavelength is...{wavelength_to_color(wave_length)}")
print()

# stock_emailalert

This script is used to notify friends and myself about how our stock(NDQ) performed over the day. 

- More of an exercise for myself rather then something I needed. I have many Apps that give me the information I need.
- I got to practice with HTML parsing which is something I don't usually get to do (Not that I will want to again after doing this)
- Also got to practice how to send test emails out which is useful.


## Changes you need to make

- There a couple "fill in" spots on the script.
- Ensure you have your gmail account setup correctly so you can do this setting as described in the script comments.
(Just create a dummy account and run everything from there).
- Ensure you update email destinations.
- I run this via cronjob everyday(except weekends) on a Raspberry Pi that I keep running most of the time.
- If you want to capture a different stock, you will need to:
    -  Change URL you are pulling data from.
    -  Change div names to tell it where to look.
    -  Can change variable names for it to make more sense.
    -  Check my working example of NDQ in the script as a comparison.





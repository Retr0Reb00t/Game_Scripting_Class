--[[
    Author: Clarece Isaiah Franklin
    Date: Jun-25-2025
    Purpose: Print out user input in all caps
--]]


-- Declare variables
local userInput


--[[ Creates a loop that only stops when the user inputs a valid 
    message that can be capitalized --]]
while( userInput == nil or userInput == string.upper(userInput))
do
    -- Asks user to input a message and store it in userInput
    io.write("What do you want to capitilize?: ")
    userInput = io.read()
end


-- Capitalizes and stores the userInput variable
userInput = string.upper(userInput)

-- Prints out capitalized message
print("Your message: ".. userInput)



--[[
    Author: Clarece Isaiah Franklin
    Date: Jun-25-2025
    Purpose: Print out the sum of two user inputted numbers
--]]


-- Returns a user inputted number
local function getANumber()
    -- Declare function variables
    local num

    -- Creates a loop that only stops when the num variable has a number in it
    while(num == nil or type(num) ~= "number")
    do
        -- Asks user to input a number and stores it in num
        io.write("Input a number: ")
        num = tonumber(io.read())
    end

    return num
end


-- Declare variables
local userNumberOne, userNumberTwo


-- Stores user inputted numbers in variables
userNumberOne = getANumber()
userNumberTwo = getANumber()

-- Prints out the sum of the two numbers
print(userNumberOne .. " + " .. userNumberTwo .. " = " .. userNumberOne + userNumberTwo)

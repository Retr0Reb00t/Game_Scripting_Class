--[[
    Author: Clarece Isaiah Franklin
    Date: Jun-26-2025
    Purpose: Ask user to print out a number and print out left or right
--]]


-- Declare variables
local num
local leftNum = 0
local rightNum = 0


-- Loops 10 times
for i = 1, 10, 1 do
    
    -- Loops until num is a whole number
    while(num == nil or math.type(num) ~= "integer")
    do
        -- Asks user to input a whole number and stores it in num
        io.write("Input a whole number: ")
        num = tonumber(io.read())
    end

    -- If num is even
    if(num % 2 == 0) then
        -- Print right and add to rightNum
        print("Right\n")
        rightNum = rightNum + 1
    else -- If num is odd
        -- Print left and add to leftNum
        print("Left\n")
        leftNum = leftNum + 1
    end
    
    -- Resets num
    num = nil
end

-- Prints out how many times right and left was printed
print("Printed Right: " .. rightNum)
print("Printed Left: " .. leftNum)
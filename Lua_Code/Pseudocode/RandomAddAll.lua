--[[
    Author: Clarece Isaiah Franklin
    Date: Jun-26-2025
    Purpose: Get a random amount of numbers and get their sum
--]]


-- Declare variables
local addUp = 0
local addMore = true
local num
local answer


-- Creates loop that only stops when addMore is false
while(addMore)
do
    -- Creates loop that ends when num equals a number
    while(num == nil or type(num) ~= "number")
    do
        -- Asks user to input a number and stores it in num
        io.write("Input a number: ")
        num = tonumber(io.read())
    end

    -- Adds number to addUp and sets num to nil
    addUp = addUp + num
    num = nil


    -- Loops while answer doesn't equal yes or no
    while(answer ~= "yes" and answer ~= "no")
    do
        -- Asks the user if they want to continue and stores there input in answer
        io.write("Do you want to add another number?(yes or no): ")
        answer = io.read()
    end

    -- If answer is no
    if(answer == "no") then
        -- Set addMore to false
        addMore = false
    else -- If answer is false
        -- Reset answer
        answer = nil
    end
end


print("Sum: " .. addUp)
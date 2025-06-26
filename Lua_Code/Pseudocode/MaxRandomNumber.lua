--[[
    Author: Clarece Isaiah Franklin
    Date: Jun-26-2025
    Purpose: Ask user to define a max number and prints
        out a random number from 0 to max number
--]]


-- Declare variables
local maxNum
local playAgain = true
local answer


-- Loops while playAgain is equal to true
while(playAgain)
do
    -- Loops until maxNum is equal to a whole number
    while(maxNum == nil or math.type(maxNum) ~= "integer")
    do
        -- Asks user to input a whole number and stores it in num
        io.write("Input a whole number: ")
        maxNum = tonumber(io.read())
    end

    -- Creates randimization seed and prints out random number
    math.randomseed(os.time())
    print("Random Number from 0 to " .. maxNum .. ": " .. math.random(0, maxNum + 1))

    -- Loops while answer doesn't equal yes or no
    while(answer ~= "yes" and answer ~= "no")
    do
        -- Asks the user if they want to continue and stores there input in answer
        io.write("Do you want to play again?(yes or no): ")
        answer = io.read()
    end

    -- if answer is no
    if(answer == "no") then
        -- sets playAgain to false
        playAgain = false
    else -- if answer is yes
        -- resets maxNum and answer
        maxNum = nil
        answer = nil
    end
end

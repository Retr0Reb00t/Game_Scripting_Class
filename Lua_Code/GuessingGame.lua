--[[
    Author: Clarece Isaiah Franklin
    Date: Jun-26-2025
    Purpose: Create a game where the user has to guess a random number
--]]


-- Declare Variables
local playAgain = true
local win = false
local guessesLeft = 7
local randNum, userGuess, answer


-- Loops until playAgain equals false
while(playAgain)
do

    -- Creates randomly generated number and stores it in randomNum
    math.randomseed(os.time())
    randNum = math.random(0,100)

    
    -- Loops until user runs out of guesses or guesses correctly
    while(guessesLeft ~= 0 and win == false)
    do
        -- Loops until the user inputs a whole number
        while(userGuess == nil or math.type(userGuess) ~= "integer")
        do
            -- Asks and stores a whole number in userGuess
            io.write("Guess a whole number: ")
            userGuess = tonumber(io.read())
        end


        -- If user guesses correctly
        if(userGuess == randNum) then
            -- Sets win to true
            win = true
        elseif(userGuess < randNum) then -- If the user's guess is smaller

            -- Resets userGuess
            userGuess = nil
            guessesLeft = guessesLeft - 1 -- removes one from guessLeft

            --[[Prints out that their guess was too small and how many 
                guesses they have left]]
            print("Too Small. " .. guessesLeft .. " guesses left\n")
        else -- If the user's guess is bigger
        
            -- Resets userGuess
            userGuess = nil
            guessesLeft = guessesLeft - 1 -- removes one from guessLeft

            --[[Prints out that their guess was too big and how many 
                guesses they have left]]
            print("Too Big. " .. guessesLeft .. " guesses left\n")
        end
    end

    -- If the user won
    if(win) then
        print("\nYou Win!\n\n")
    else -- If the user lost
        print("You Lose!\n\n")
    end


    -- Loops while answer doesn't equal yes or no
    while(answer ~= "yes" and answer ~= "no")
    do
        -- Asks the user if they want to continue and stores there input in answer
        io.write("Do you want to play again?(yes or no): ")
        answer = io.read()
    end

    -- if the user answers no
    if(answer == "no") then
        -- sets playAgain to false
        playAgain = false
    else -- if the user answers yes
    
        -- Sets variables to their original states to start another game
        guessesLeft = 7
        answer = nil
        userGuess = nil
        win = false
        print("\n\n")
    end
end
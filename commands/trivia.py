import discord
from discord.ext import commands
import requests
import json
from random import shuffle
import html

class Trivia:
    class Player(object):
        id = ""
        score = 0
        name = ""
        def __init__(self,id,score,name):
            self.id = id
            self.score = 0
            self.name = name
            
    def __init__(self,bot):
        self.bot = bot
        self.session_token = requests.get('https://opentdb.com/api_token.php?command=request').json()["token"]
        self.points = 0
        self.players = []
        self.correct = 0
        self.correct_sent = ""
        self.answered = True
        self.responses = 0
        self.win = 200

    def scoreboard(self):
        msg  = "The current scores are:\n" + "```"
        for i in self.players:
            msg += i.name + ": " + str(i.score) + "\n"
        msg += "```"
        return msg
        
    def nextq(self):
        if not self.players:
            msg = "No players are currently in the queue. Type \"!trivia join\" to enter"
            return msg
        if self.answered == False:
            msg = "There is already an active question. Please answer that one."
            return msg
        self.answered = False
        r = requests.get('https://opentdb.com/api.php?amount=1&type=multiple&token=' + self.session_token)
        difficulty = r.json()["results"][0]["difficulty"]
        if difficulty == "easy":
            self.points = 10
        elif difficulty == "medium":
            self.points = 30
        elif difficulty == "hard":
            self.points = 50
        question = r.json()["results"][0]["question"]
        correct = r.json()["results"][0]["correct_answer"]
        answers = r.json()["results"][0]["incorrect_answers"]
        category = r.json()["results"][0]["category"]
        question = html.unescape(question)
        answers.append(correct)
        shuffle(answers)
        self.correct_sent = correct
        for i in range(0,4):
            answers[i] = html.unescape(answers[i])
            if answers[i] == correct:
                self.correct = i

        msg = "This is a(n) " + difficulty + " question. The category is " + category + ". ```" + question + "```" + "```A)" + answers[0] + "\nB)" + answers[1] + "\nC)" + answers[2] + "\nD)" + answers[3] +  "```"
        return msg

    @commands.group(
        name='trivia',
        aliases=[],
        description='Simple Trivia Game',
        brief='Trivia!',
        pass_context = True,
        invoke_without_command = True
        
    )

    async def trivia(self,ctx,*,message):
        msg = "Please Join or Start the game!"
        await self.bot.say(msg)

    @trivia.command(
        name = 'queue',
        aliases = ['list','whoplays'],
        description = "Queue of players",
        brief = "Current Players"
    )
    async def queue(self):
        msg = ""
        if not self.players:
            await self.bot.say("No current players.")
            return
        for i in self.players:
            msg += i.name + ": " + str(i.score) + "\n"
        await self.bot.say(msg)

    @trivia.command(
        name = 'join',
        aliases=[],
        description = 'Join the Queue for the Trivia Game',
        brief = 'Join Trivia',
        pass_context = True
    )
    async def join(self,ctx):
        for i in self.players:
            if i.id == ctx.message.author.id:
                await self.bot.say("You are already in the queue.")
                return
        for server in self.bot.servers:
            for member in server.members:
                if ctx.message.author.id == member.id:
                    name = member.name
                    break
            else:
                continue
            break
        new_player = self.Player(ctx.message.author.id,0,name)
        self.players.append(new_player)
        msg = "Current Players are: "
        for i in self.players:
            msg += '<@' + str(i.id) + '> '
        await self.bot.say(msg)
    
    @trivia.command(
        name = 'question',
        aliases=['q','ques','next'],
        description = 'This command grabs the next question.',
        brief = 'Next Question'
    )

    async def question(self):
        await self.bot.say(self.nextq())
        return
        if not self.players:
            await self.bot.say("No players are currently in the queue. Type \"!trivia join\" to enter")
            return
        if self.answered == False:
            await self.bot.say("There is already an active question. Please answer that one.")
            return
        self.answered = False
        r = requests.get('https://opentdb.com/api.php?amount=1&type=multiple&token=' + self.session_token)
        difficulty = r.json()["results"][0]["difficulty"]
        if difficulty == "easy":
            self.points = 10
        elif difficulty == "medium":
            self.points = 30
        elif difficulty == "hard":
            self.points = 50
        question = r.json()["results"][0]["question"]
        correct = r.json()["results"][0]["correct_answer"]
        answers = r.json()["results"][0]["incorrect_answers"]
        category = r.json()["results"][0]["category"]
        question = html.unescape(question)
        answers.append(correct)
        shuffle(answers)
        self.correct_sent = correct
        for i in range(0,4):
            answers[i] = html.unescape(answers[i])
            if answers[i] == correct:
                self.correct = i
            
        msg = "This is a(n) " + difficulty + " question. The category is " + category + ". ```" + question + "```" + "```A)" + answers[0] + "\nB)" + answers[1] + "\nC)" + answers[2] + "\nD)" + answers[3] +  "```" 
        await self.bot.say(msg)
    

    @trivia.command(
        name = "a",
        aliases = ["A"],
        description = "Answer Choice A",
        brief = "Choice A",
        pass_context = True

    )
    async def a(self,ctx):
        if self.answered == True:
            await self.bot.say("There is no active question. Please type \"!trivia question\" for a new question")
            return
        for i in range(0,len(self.players)):
            if(ctx.message.author.id == self.players[i].id):
                if self.correct == 0:
                    self.players[i].score += self.points
                    break
            elif(i == (len(self.players))):
                await self.bot.say("You are not in the queue and cannot answer this question.")
                return
        self.responses+=1
        if(self.responses == (len(self.players))):
            msg  = "```The correct answer was " + self.correct_sent + "```"
            msg += " " + self.scoreboard()
            self.responses = 0
            self.points = 0
            self.answered = True
            await self.bot.say(msg)
            for i in range(0,len(self.players)):
                if self.players[i].score >= self.win:
                    msg = "```" + self.players[i].name + "wins!"
                    self.players = []
                    return
            await self.bot.say(self.nextq())

    @trivia.command(
        name = "b",
        aliases = ["B"],
        description = "Answer Choice B",
        brief = "Choice B",
        pass_context = True

    )
    async def b(self,ctx):
        if self.answered == True:
            await self.bot.say("There is no active question. Please type \"!trivia question\" for a new question")
            return
        for i in range(0,len(self.players)):
            if(ctx.message.author.id == self.players[i].id):
                if self.correct == 1:
                    self.players[i].score += self.points
                    break
            elif(i == len(self.players)):
                await self.bot.say("You are not in the queue and cannot answer this question.")
                return
        self.responses+=1
        if(self.responses == (len(self.players))):
            msg  = "```The correct answer was " + self.correct_sent + "```"
            msg += " " + self.scoreboard()
            self.responses = 0
            self.points = 0
            self.answered = True
            await self.bot.say(msg)
            for i in range(0,len(self.players)):
                if self.players[i].score >= self.win:
                    msg = "```" + self.players[i].name + "wins!"
                    self.players = []
                    return
            await self.bot.say(self.nextq())

    @trivia.command(
        name = "c",
        aliases = ["C"],
        description = "Answer Choice C",
        brief = "Choice C",
        pass_context = True

    )
    async def c(self,ctx):
        if self.answered == True:
            await self.bot.say("There is no active question. Please type \"!trivia question\" for a new question")
            return
        for i in range(0,len(self.players)):
            if(ctx.message.author.id == self.players[i].id):
                if self.correct == 2:
                    self.players[i].score += self.points
                    break
            elif(i == len(self.players)):
                await self.bot.say("You are not in the queue and cannot answer this question.")
                return
        self.responses+=1
        if(self.responses == (len(self.players))):
            msg  = "```The correct answer was " + self.correct_sent + "```"
            msg += " " + self.scoreboard()
            self.responses = 0
            self.points = 0
            self.answered = True
            await self.bot.say(msg)
            for i in range(0,len(self.players)):
                if self.players[i].score >= self.win:
                    msg = "```" + self.players[i].name + "wins!"
                    self.players = []
                    return
            await self.bot.say(self.nextq())

    @trivia.command(
        name = "d",
        aliases = ["D"],
        description = "Answer Choice D",
        brief = "Choice D",
        pass_context = True

    )
    async def d(self,ctx):
        if self.answered == True:
            await self.bot.say("There is no active question. Please type \"!trivia question\" for a new question")
            return
        for i in range(0,len(self.players)):
            if(ctx.message.author.id == self.players[i].id): 
                if self.correct == 3:
                    self.players[i].score += self.points
                    break
            elif(i == len(self.players)):
                await self.bot.say("You are not in the queue and cannot answer this question.")
                return
        self.responses+=1
        if(self.responses == (len(self.players))):
            msg  = "```The correct answer was " + self.correct_sent + "```"
            msg += " " + self.scoreboard()
            self.responses = 0
            self.answered = True
            self.points = 0
            await self.bot.say(msg)
            for i in range(0,len(self.players)):
                if self.players[i].score >= self.win:
                    msg = "```" + self.players[i].name + "wins!"
                    self.players = []
                    return
            await self.bot.say(self.nextq())
        


def setup(bot):
    bot.add_cog(Trivia(bot))

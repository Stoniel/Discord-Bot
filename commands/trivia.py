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
        self.ids = []
        self.session_token = requests.get('https://opentdb.com/api_token.php?command=request').json()["token"]
        self.points = 0
        self.players = []
        self.correct = 0
        self.correct_sent = ""
        self.answered = True
        self.responses = 0

    def scoreboard(self):
        msg  = "The current scores are:\n" + "```"
        for i in self.players:
            msg += i.name + ": " + str(i.score) + "\n"
        msg += "```"
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
        name = 'join',
        aliases=[],
        description = 'Join the Queue for the Trivia Game',
        brief = 'Join Trivia',
        pass_context = True
    )
    async def join(self,ctx):
        for i in self.players:
            if i.id == ctx.message.author.id:
                await self.bot.say("You are already in the queue, and cannot answer this question.")
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
        if not self.players:
            await self.bot.say("No players are currently in the queue. Type \"!trivia join\" to enter")
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
        for i in range(0,len(self.players)):
            if(ctx.message.author.id == self.players[i].id):
                if self.correct == 3:
                    self.players[i].score += self.points
            elif(i == len(self.players)-1):
                await self.bot.say("You are not in the queue and cannot answer this question.")
                return
        if(self.responses == (len(self.players)-1)):
            msg  = "```The correct answers was " + self.correct_sent + "```"
        msg += " " + self.scoreboard()
        await self.bot.say(msg)

    @trivia.command(
        name = "b",
        aliases = ["B"],
        description = "Answer Choice B",
        brief = "Choice B",
        pass_context = True

    )
    async def b(self,ctx):
        for i in range(0,len(self.players)):
            if(ctx.message.author.id == self.players[i].id):
                if self.correct == 1:
                    self.players[i].score += self.points
            elif(i == len(self.players)-1):
                await self.bot.say("You are not in the queue and cannot answer this question.")
                return
        if(self.responses == (len(self.players)-1)):
            msg  = "```The correct answers was " + self.correct_sent + "```"
        msg += " " + self.scoreboard()
        await self.bot.say(msg)

    @trivia.command(
        name = "c",
        aliases = ["C"],
        description = "Answer Choice C",
        brief = "Choice C",
        pass_context = True

    )
    async def c(self,ctx):
        for i in range(0,len(self.players)):
            if(ctx.message.author.id == self.players[i].id):
                if self.correct == 2:
                    self.players[i].score += self.points
            elif(i == len(self.players)-1):
                await self.bot.say("You are not in the queue and cannot answer this question.")
                return
        if(self.responses == (len(self.players)-1)):
            msg  = "```The correct answers was " + self.correct_sent + "```"
        msg += " " + self.scoreboard()
        await self.bot.say(msg)

    @trivia.command(
        name = "d",
        aliases = ["D"],
        description = "Answer Choice D",
        brief = "Choice D",
        pass_context = True

    )
    async def d(self,ctx):
        for i in range(0,len(self.players)):
            if(ctx.message.author.id == self.players[i].id): 
                if self.correct == 3:
                    self.players[i].score += self.points
            elif(i == len(self.players)-1):
                await self.bot.say("You are not in the queue and cannot answer this question.")
                return
        if(self.responses == (len(self.players)-1)):
            msg  = "```The correct answers was " + self.correct_sent + "```"
        msg += " " + self.scoreboard()
        await self.bot.say(msg)
        


def setup(bot):
    bot.add_cog(Trivia(bot))

from discord.errors import Forbidden
import json
import random
import re
import requests


async def _sendEmbed(ctx, embed):

    try:
        await ctx.send(embed=embed)
    except Forbidden:
        try:
            await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
        except Forbidden:
            await ctx.author.send(
                f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
                f"May you inform the server team about this issue? :slight_smile: ", embed=embed)


def _getPrefix1(client, message):
    with open('src/server_config.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]['prefix']


def _textFormatting(text):
    # Basially removed non ASCII codes and then removing extra spaces
    text = ''.join([i if ord(i) < 128 else ' ' for i in text])
    text = re.sub('\s+', ' ', text)
    text = repr(text)
    return text


def _isValid(username: str):
    user_object = requests.get(
        f"https://codeforces.com/api/user.info?handles={username}")
    data = json.loads(user_object.text)
    status = data["status"]

    if status == 'OK':
        return data
    else:
        return False


def _userInfo(obj: dict):
    default_obj = {
        "lastName": "-",
        "country": "-",
        "lastOnlineTimeSeconds": 0,
        "city": "-",
        "rating": 0,
        "friendOfCount": 0,
        "titlePhoto": "-",
        "handle": "-",
        "avatar": "-",
        "firstName": "-",
        "contribution": 0,
        "organization": "-",
        "rank": "-",
        "maxRating": 0,
        "registrationTimeSeconds": 0,
        "maxRank": "-"
    }
    if len(default_obj) == len(obj):
        return obj
    else:
        key_obj = list(obj)
        for i in key_obj:
            default_obj[i] = obj[i]
    return default_obj


def _getProblem(rating: int, tags: list):
    tag_str = ""
    for tag in tags:
        tag_str += f"{tag};"
    tag_str = tag_str[:-1]
    data = requests.get(
        f"https://codeforces.com/api/problemset.problems?tags={tag_str}")
    data = json.loads(data.text)
    data = data["result"]

    problems = data['problems']

    if not problems:
        return "Sorry no problem found under given arguments"

    req_problems = []

    for prob in problems:
        if ('rating' in prob.keys()) and rating == prob['rating']:
            req_problems.append(prob)

    if not req_problems:
        return "Sorry no problem found under given arguments"

    l = len(req_problems)
    index = random.randint(0, l-1)

    return req_problems[index]


def _getPrefix2(ctx):
    with open('src/server_config.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(ctx.guild.id)]['prefix']


def _getChannelId(ctx):
    with open('src/server_config.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(ctx.guild.id)]['channel_id']


def _getRoleId(ctx):
    with open('src/server_config.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(ctx.guild.id)]['role_id']


def _isValidPrefix(prefix):
    if len(prefix) > 1:
        return False
    else:
        prefix = ord(prefix)
        if (prefix > 47 and prefix < 58) or (prefix > 64 and prefix < 91) or (prefix > 96 and prefix < 123):
            return False
        else:
            return True


def _isValidChannel(ctx, channelid):
    channelid = int(channelid)
    channelid = ctx.bot.get_channel(channelid)
    print(channelid)
    if channelid != None:
        return True
    return False


def _isValidRole(ctx, roleid):
    roleid = int(roleid)
    print(f'insied {roleid}')
    roleid = ctx.guild.get_role(roleid)

    if roleid != None:
        return True
    return False

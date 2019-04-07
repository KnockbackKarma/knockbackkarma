const Discord = require('discord.js')
const client = new Discord.Client()

client.on('ready', () => {
    console.log("Connected as " + client.user.tag) //puts a message in the terminal to tell you if the bots online.

    client.user.setActivity("myself trying to code", {type: "WATCHING"}) //sets the playing status

    client.guilds.forEach((guild) => {
        console.log(guild.name)
        guild.channels.forEach((channel) => {
            console.log(` - ${channel.name} ${channel.type} ${channel.id}`)
        })
        // General channel id: 564176276659634189
    })

    let generalChannel = client.channels.get("564176276659634189")
    generalChannel.send("ur mum gaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaay")
})


client.login("process.emv.TOKEN")

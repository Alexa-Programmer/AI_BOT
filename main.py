import discord
from discord.ext import commands
from model import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Saved the image to ./{attachment.filename}")
            result = get_class(model_path='model.h5',labels_path='labels.txt', image_path=f"Saved the image to ./{attachment.filename}")
            if result == "Yaz":
                await ctx.send("""Yaz Meyvelerinin Genel Özellikleri
Mevsim: Haziran – Eylül arasında olgunlaşır.

Su oranı yüksek: Sıcağın etkisini azaltır, vücudu serinletir. Genellikle %80’in üzerinde su içerirler.

Vitamin açısından zengin: Özellikle C vitamini , A vitamini ve antioksidanlar bol miktarda bulunur.

Mineral kaynağı: Potasyum , magnezyum ve demir içerebilir.

Düşük kalori: Çoğu yaz meyvesi düşük kalorili olduğu için hem tatlı ihtiyacını karşılar hem de kilo kontrolünü destekler.

Lifli yapıda: Sindirim sistemini düzenler, tokluk hissi verir.""")
            elif result == "İlkbahar":
                await ctx.send("""İlkbahar Meyvelerinin Genel Özellikleri
Mevsim: Mart – Mayıs arası olgunlaşırlar.

Taze başlangıç: Kış sonrası vitamin ve mineral eksikliğini tamamlamada önemli rol oynarlar.

Vitamin açısından zengin: Özellikle C vitamini (bağışıklık), A vitamini (göz ve cilt), B grubu vitaminler (enerji üretimi).

Antioksidan kaynağı: Vücudu serbest radikallerin zararlı etkilerinden korur.

Orta düzeyde su içerir: Yaz meyveleri kadar sulu değiller ama yine de ferahlatıcıdır.

Lif bakımından zengin: Sindirimi düzenler, tok tutar.

Mevsim geçişine uyum sağlar: Alerji, yorgunluk ve bağışıklık zayıflamasına karşı koruyucu etkileri vardır.

""")
            elif result == "Kış":
                await ctx.send("""Kış Meyvelerinin Genel Özellikleri
Mevsim: Aralık – Şubat ayları arasında en bol dönemlerini yaşarlar.

Soğuğa dayanıklı: Düşük sıcaklıklarda gelişir, bazıları depolama ile uzun süre taze kalabilir.

C vitamini deposu: Soğuk algınlığı ve grip gibi kış hastalıklarına karşı bağışıklığı güçlendirir.

Enerji verici: Yaz meyvelerine göre şeker oranı biraz daha yüksek olabilir, vücudu soğuk havalarda enerjik tutar.

Lif açısından zengin: Sindirimi düzenler ve tokluk sağlar.

Antioksidan kaynağı: Vücudu serbest radikallerden korur, cilt sağlığını destekler.

Depolanabilir: Elma, armut gibi bazı kış meyveleri aylarca bozulmadan saklanabilir.""")
            elif result == "Sonbahar":
                await ctx.send("""Sonbahar Meyvelerinin Genel Özellikleri
Mevsim: Eylül – Kasım ayları arası olgunlaşır.

Geçiş dönemi besinleri: Yazın hafif, sulu meyvelerinden kışın daha yoğun ve besleyici meyvelerine geçişi sağlar.

Vitamin ve mineral açısından zengin: Özellikle C vitamini (bağışıklık), A vitamini (göz sağlığı), potasyum ve lif içerikleri yüksek.

Bağışıklık güçlendirici: Mevsim geçişlerinde soğuk algınlığına karşı koruma sağlar.

Orta su oranı: Yaz meyvelerinden daha az, kış meyvelerinden biraz daha fazla su içerir.

Antioksidan açısından güçlü: Hücre yenilenmesini ve cilt sağlığını destekler.""")
            else:
                await ctx.send(f"Tanımlanamayan Sınıf: {result} ")
    else:
        await ctx.send("You forgot to upload the image :(")


bot.run(TOKEN)

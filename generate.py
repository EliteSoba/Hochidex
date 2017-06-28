class Char():
	NAME = ""
	DEFENSE = 0
	GUTS = 0
	HP = 0
	BDASH_DUR = 0
	BDASH_INVUL = ""
	JUMP = 0
	FUWU = 0
	FDWU = 0
	HOCHI = [("??", False), ("??", False), ("??", False), ("??", False), ("??", False), ("??", False)]
	
	def __init__(self, name="", defense=0, guts=0, hp=0, bdash_d=0, bdash_i="", jump=0, fuwu = 0, fdwu = 0):
		self.NAME = name
		self.DEFENSE = defense
		self.GUTS = guts
		self.HP = hp
		self.BDASH_DUR = bdash_d
		self.BDASH_INVUL = bdash_i
		self.JUMP = jump
		self.FUWU = fuwu
		self.FDWU = fdwu

def main():
	guts = [(.9,.76,.6,.5,.4), (.87,.72,.58,.48,.4), (.84,.68,.56,.46,.38), (.81,.66,.54,.44,.38), (.78,.64,.5,.42,.38), (.75,.6,.48,.4,.36)]
	chars = {}
	chars["answer"] = Char(name="Answer", defense=1.03, guts=0, bdash_d=21, bdash_i="1-12 Strike", jump=3, fuwu=24, fdwu=24)
	chars["answer"].HOCHI=[
	("2S > 2HS(2)", True),
	("2S > 2HS(2)", True),
	("5K > 2HS(2)", True),
	("2S > 2HS(1)", True),
	("2S > 2HS(2)", False),
	("5K > 2HS(2)", True)]
	
	chars["axl"] = Char(name="Axl Low", defense=1.06, guts=1, bdash_d=16, bdash_i="1-8 Strike | 1-16 Airborne", jump=4, fuwu=25, fdwu=21)
	chars["axl"].HOCHI=[
	("2S > 2HS(1) > Delay", True),
	("2S > 2HS(1) > Delay", True),
	("??", False),
	("??", False),
	("??", False),
	("??", False)]
	
	chars["baiken"] = Char(name="Baiken", defense=1.18, guts=4, bdash_d=16, bdash_i="1-8 Strike | ?? Airborne", jump=3, fuwu=22, fdwu=21)
	chars["baiken"].HOCHI=[
	("2K > 2HS(2)", True),
	("2K > 2HS(2)", True),
	("2S > 2HS(1)", False),
	("2S > 2HS(2)", True),
	("2S > 2HS(2)", False),
	"2K > 2HS(2)", False)]
	
	chars["bedman"] = Char(name="Bedman", defense=.98, guts=0, bdash_d=23, bdash_i="1-10 Strike | 11-19 Foot", jump=3, fuwu=24, fdwu=30)
	chars["bedman"].HOCHI=[("2S > 2HS(2)", True),
	("2S > 2HS(2)", True),
	("2S > 2HS(2)", True),
	("2S > 2HS(2)", False),
	("c.S > 2S > 2HS(1)", True),
	("2S > 2HS(2)", True)]
	
	chars["chipp"] = Char(name="Chipp Zanuff", defense=1.3, guts=4, bdash_d=21, bdash_i="1-9 Strike | 1-21 Airborne", jump=3, fuwu=30, fdwu=24)
	chars["chipp"].HOCHI=[("2S > 5K > 2HS(1)", True),
	("2S > 5K > 2HS(1)", True),
	("6P(1) > 2HS(1)", True),
	("2S > 2HS(2)", True),
	("c.S > 2S > 2HS(1)", False),
	("2S > 2HS(2)", True)]
	
	chars["dizzy"] = Char(name="Dizzy", defense=1.06, guts=1, bdash_d=16, bdash_i="1-9 Strike | 1-13 Airborne", jump=3, fuwu=25, fdwu=24)
	chars["dizzy"].HOCHI=[("2S > 2HS(1)", False),
	("2S > 2HS(1)", False),
	("5K > 2HS(1)", False),
	("2S > 2HS(1)", True),
	("2S > 2HS(2)", False),
	("2S > 2HS(1)", False)]
	
	chars["elphelt"] = Char(name="Elphelt Valentine", defense=1.03, guts=0, bdash_d=13, bdash_i="1-9 Strike | 1-13 Airborne", jump=3, fuwu=27, fdwu=27)
	chars["elphelt"].HOCHI=[("2S > 2HS(2) > Delay", False),
	("2S > 2HS(2) > Delay", False),
	("2S > 2HS(1)", False),
	("2S > 2HS(1)", False),
	("2S > 2HS(2)", False),
	("2S > 2HS(1)", False)]
	
	chars["faust"] = Char(name="Faust", defense=1, guts=0, bdash_d=13, bdash_i="1-7 Strike | 1-13 Airborne", jump=3, fuwu=25, fdwu=29)
	chars["faust"].HOCHI=[("c.S > f.S > 2HS(1)", True),
	("c.S > f.S > 2HS(1)", True),
	("5K > 2HS(2)", True),
	("??", False),
	("c.S > f.S > 2HS(1)", False),
	("c.S > 2HS(1)", True)]
	
	chars["kum"] = Char(name="Kum Haehyun", defense=.96, guts=2, bdash_d = 16, bdash_i = "1-9 Strike | 1-15 Airborne", jump=3, fuwu=25, fdwu=27)
	chars["kum"].HOCHI=[("6K(1) > 2HS(2)", True),
	("6K(1) > 2HS(2)", True),
	("??", False),
	("c.S > f.S > 2HS(1)", False),
	("6K > 2HS(1)", True),
	("2S > 2HS(1)", False)]
	
	chars["ino"] = Char(name="I-No", defense=1.06, guts=1, bdash_d=16, bdash_i = "1-8 Strike | 1-16 Airborne", jump=3, fuwu=24, fdwu=20)
	chars["ino"].HOCHI=[("2S > 2HS(1)", True),
	("2S > 2HS(1)", True),
	("2S > 2HS(1)", True),
	("2S > 2HS(1)", True),
	("2S > 2HS(1)", True),
	("2S > 2HS(1)", True)]
	
	chars["jacko"] = Char(name="Jack-O'", defense=1.03, guts=2, bdash_d=14, bdash_i="1-9 Strike | 1-13 Airborne", jump=3, fuwu=25, fdwu=23)
	chars["jacko"].HOCHI=[("2S > 2HS(1)", True),
	("2S > 2HS(1)", True, "Weird"),
	("2S > 2HS(1)", True),
	("2S > 2HS(1)", True),
	("2S > 2HS(1)", True),
	("2S > 2HS(1)", True)]
	
	chars["jam"] = Char(name="Jam Kuradoberi", defense=1.06, guts=3, bdash_d=13, bdash_i="1-7 Strike | 1-12 Airborne", jump=3, fuwu=26, fdwu=25)
	chars["jam"].HOCHI=[("2K > 2HS(2) > Delay", True),
	("2K > 2HS(2) > Delay", True),
	("5K > 2HS(2)", False),
	("2S > 2HS(1)", True),
	("2S > 2HS(1)", True),
	("2S > 2HS(1)", True)]
	
	chars["johnny"] = Char(name="Johnny", defense=1, guts=3, bdash_d=11, bdash_i="1-7 Strike | 1-10 Airborne", jump=4, fuwu=25, fdwu=24)
	chars["johnny"].HOCHI=[("2S > 2HS(2)", True),
	("2S > 2HS(2)", True),
	("2S > 2HS(2)", True),
	("2S > 2HS(2)", False),
	("2S > 2HS(2)", False),
	("2S > 2HS(2)", True)]
	
	chars["ky"] = Char(name="Ky Kiske", defense=1.03, guts=2, bdash_d=16, bdash_i="1-9 Strike | 1-16 Airborne", jump=3, fuwu=23, fdwu=21)
	chars["ky"].HOCHI=[("2S > 2HS(2)", True),
	("2S > 2HS(2)", True),
	("2S > 2HS(2)", True),
	("2S > 2HS(2)", True),
	("c.S > 6K > 2HS(1)", True),
	("2S > 2HS(2)", True)]
	
	chars["leo"] = Char(name="Leo Whitefang", defense=1, guts=3, bdash_d=16, bdash_i="1-9 Strike | 1-15 Airborne", jump=4, fuwu=28, fdwu=26)
	chars["leo"].HOCHI=[("c.S > 2S > 2HS(1)", True),
	("c.S > 2S > 2HS(1)", True),
	("c.S > 2S > 2HS(1)", True),
	("2S > 2HS(2)", False),
	("c.S > 5HS(1) > 2HS(1)", True),
	("??", False)]
	
	chars["may"] = Char(name="May", defense=1.06, guts=3, bdash_d=13, bdash_i="1-9 Strike | 1-13 Airborne", jump=3, fuwu=25, fdwu=22)
	chars["may"].HOCHI=[("2S > 2HS(2) > Delay", True),
	("2S > 2HS(2) > Delay", True),
	("5K > 2HS(1)", True, "Weird"),
	("2S > 2HS(1)", True),
	("2S > 2HS(2)", False),
	("5K > 2HS(2)", True)]
	
	chars["millia"] = Char(name="Millia Rage", defense=1.21, guts=3, bdash_d=11, bdash_i="1-5 Strike | 1-11 Airborne", jump=3, fuwu=25, fdwu=23)
	chars["millia"].HOCHI=[("2S > 2HS(1)", True),
	("2S > 2HS(1)", True),
	("2S > 2HS(1)", False),
	("2S > 2HS(1)", True),
	("2S > 2HS(2)", False),
	("2S > 2HS(1)", False)]
	
	chars["potemkin"] = Char(name="Potemkin", defense=.93, guts=3, bdash_d=21, bdash_i="1-20 Strike | 1-21 Airborne", jump=5, fuwu=24, fdwu=22)
	chars["potemkin"].HOCHI=[("c.S > f.S > 2HS(1)", True),
	("c.S > f.S > 2HS(1)", True),
	("c.S > f.S > 2HS(1)", True),
	("c.S > 2HS(1)", False),
	("6K > 2HS(2)", True),
	("c.S > f.S > 2HS(1)", True)]
	
	chars["ramlethal"] = Char(name="Ramlethal Valentine", defense=1.06, guts=1, bdash_d=16, bdash_i="1-9 Strike | 1-16 Airborne", jump=3, fuwu=25, fdwu=23)
	chars["ramlethal"].HOCHI=[("2S > 2HS(1)", False),
	("2S > 2HS(1)", False),
	("2S > 2HS(1)", False),
	("2S > 2HS(1)", False),
	("2S > 2HS(1)", False),
	("2S > 2HS(1)", False)]
	
	chars["raven"] = Char(name="Raven", defense=1.1, guts=5, bdash_d=21, bdash_i="1-9 Strike | 1-20 Airborne", jump=3, fuwu=25, fdwu=24)
	chars["raven"].HOCHI=[("c.S > f.S > 2HS(1)", True),
	("c.S > f.S > 2HS(1)", True),
	("2S > 2HS(1)", True),
	("2S > 2HS(2)", True),
	("6K > 2HS(1)", True),
	("2S > 2HS(2)", True)]
	
	chars["sin"] = Char(name="Sin Kiske", defense=1.04, guts=1, bdash_d=24, bdash_i="1-16 Strike | 1-18 Throw", jump=3, fuwu=30, fdwu=21)
	chars["sin"].HOCHI=[("2S > 2HS(2)", True),
	("2S > 2HS(2)", True),
	("5K > 2HS(2)", True),
	("2S > 2HS(1)", True),
	("2S > 2HS(2)", False),
	("5K > 2HS(2)", True)]
	
	chars["slayer"] = Char(name="Slayer", defense=.96, guts=1, bdash_d=28, bdash_i="1-19 Full | 20 Strike", jump=4, fuwu=26, fdwu=20)
	chars["slayer"].HOCHI=[("2S > 5K > 2HS(1)", True),
	("2S > 5K > 2HS(1)", True),
	("2S > 2HS(2)", True),
	("2S > 2HS(1)", True),
	("c.S > 2HS(2)", False),
	("2S > 2HS(2)", True)]
	
	chars["sol"] = Char(name="Sol Badguy", defense=1, guts=1, bdash_d=16, bdash_i="1-8 Strike | 1-16 Airborne", jump=3, fuwu=25, fdwu=21)
	chars["sol"].HOCHI=[("2S > 5K > 2HS(1)", True),
	("c.S > 2HS(2)", True),
	("6P(1) > 2HS(1)", True),
	("Wait > 6P(1) > 2HS(1)", False),
	("c.S > 2S > 2HS(1)", False),
	("2S > 2HS(1)", True)]
	
	chars["venom"] = Char(name="Venom", defense=1.03, guts=1, bdash_d=13, bdash_i="1-7 Strike | 1-13 Airborne", jump=4, fuwu=21, fdwu=26)
	chars["venom"].HOCHI=[("2S > 6K > 2HS(1)", True),
	("2S > 2HS(2)", True),
	("c.S > 2HS(1)", True),
	("2S > 2HS(2)", True),
	("c.S > 2HS(2)", True),
	("2S > 2HS(2)", True)]
	
	chars["zato"] = Char(name="Zato-1", defense=1.09, guts=0, bdash_d=16, bdash_i="1-7 Strike | 1-16 Airborne", jump=3, fuwu=25, fdwu=22)
	chars["zato"].HOCHI=[("2S > 2HS(2)", True),
	("2S > 2HS(2)", True),
	("5K > 2HS(2)", True),
	("Wait > 5K > 2HS(2)", True, "Hard"),
	("c.S > 2S > 2HS(1) > Delay", True),
	("2S > 2HS(2)", True)]
	
	
	
	file = open("template.html", "r")
	template = "".join(file.readlines())
	file.close()
	for name in chars:
		char = chars[name]
		g = guts[char.GUTS]
		hp = 210 + 42/g[0] + 42/g[1] + 42/g[2] + 42/g[3] + 42/g[4]
		hp /= char.DEFENSE
		char.HP = int(hp+0.5)
		
		content = template.replace("{{ NAME }}", char.NAME)
		content = content.replace("{{ DEFENSE }}", "%1.2f" % char.DEFENSE)
		content = content.replace("{{ GUTS }}", str(char.GUTS))
		content = content.replace("{{ HP }}", str(char.HP))
		content = content.replace("{{ BDASH_DUR }}", str(char.BDASH_DUR))
		content = content.replace("{{ BDASH_INVUL }}", char.BDASH_INVUL)
		content = content.replace("{{ JUMP }}", str(char.JUMP))
		content = content.replace("{{ FUWU }}", str(char.FUWU))
		content = content.replace("{{ FDWU }}", str(char.FDWU))
		if name == "leo":
			content = content.replace("{{ LEO }}", "\t<div class=\"row main\">\n\t\t<div class=\"col-sm-6\">\n\t\tStance BDash Duration: 16\n\t\t</div>\n\t\t<div class=\"col-sm-6\">\n\t\tStance BDash Invul: 1-13 Full\n\t\t</div>\n\t</div>")
		else:
			content = content.replace ("{{ LEO }}", "")
		for i, h in enumerate(char.HOCHI):
			content = content.replace("{{ PUFFPUFF"+str(i)+" }}", "puffpuff" if h[1] else "")
			combo = h[0]
			if len(h) > 2:
				combo += " <a href=\"#hochi"+str(i)+"\" data-toggle=\"tooltip\" title=\""+h[2]+"\" style=\"color: red; font-size: small\">[?]</a>"
			content = content.replace("{{ HOCHI"+str(i)+" }}", combo)
		output = open(name + ".html", "w")
		output.write(content)
		output.close()

if __name__ == "__main__":
	main()
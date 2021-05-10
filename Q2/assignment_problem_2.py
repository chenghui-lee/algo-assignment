# -*- coding: utf-8 -*-

# Initial setup and import the libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import nltk # nlp
import re
import plotly.graph_objects as go
import plotly.express as px
from newspaper import Article # webscrap
import plotly.graph_objects as go

company_list = ['City-Link','Pos Laju','GDex','J&T',"DHL"]
delivery_list = ["cle_text.txt","pl_text.txt","gd_text.txt","jt_text.txt","dhl_text.txt"]

class Node:
    def __init__(self):
        self.children = [None] * 256
        self.isend = False

class trie:
    def __init__(self, ):
        self.__root = Node()

    def __len__(self, ):
        return len(self.search_byprefix(''))

    def __str__(self):
        ll = self.search_byprefix('')
        string = ''
        for i in ll:
            string += i
            string += '\n'
        return string

    def chartoint(self, character):
        return ord(character) - ord('a')

    def remove(self, string):
        ptr = self.__root
        length = len(string)
        for idx in range(length):
            i = ord(string[idx])
            if ptr.children[i] is not None:
                ptr = ptr.children[i]
            else:
                raise ValueError("Keyword doesn't exist in trie")
        if ptr.isend is not True:
            raise ValueError("Keyword doesn't exist in trie")
        ptr.isend = False
        return

    def insert(self, string):
        ptr = self.__root
        length = len(string)
        for idx in range(length):
            i = ord(string[idx])
            if ptr.children[i] is not None:
                ptr = ptr.children[i]
            else:
                ptr.children[i] = Node()
                ptr = ptr.children[i]
        ptr.isend = True

    def search(self, string):
        ptr = self.__root
        length = len(string)
        for idx in range(length):
            i = ord(string[idx])
            if ptr.children[i] is not None:
                ptr = ptr.children[i]
            else:
                return False
        if ptr.isend is not True:
            return False
        return True

    def __getall(self, ptr, key, key_list):
        if ptr is None:
            key_list.append(key)
            return
        if ptr.isend == True:
            key_list.append(key)
        for i in range(256):
            if ptr.children[i] is not None:
                self.__getall(ptr.children[i], key + chr(i), key_list)

    def search_byprefix(self, key):
        ptr = self.__root
        key_list = []
        length = len(key)
        for idx in range(length):
            i = self.chartoint(key[idx])
            if ptr.children[i] is not None:
                ptr = ptr.children[i]
            else:
                return None

        self.__getall(ptr, key, key_list)
        return key_list


'''
Webscrap function to scrap informations from 3 sites for each delivery company
will output text file with the combined news for each delivery company
'''
def webscrap():
    # J&T Express (JT)
    # malay mail
    url = "https://www.malaymail.com/news/malaysia/2021/02/07/courier-company-jt-express-explains-staffs-violent-handling-of-parcels-caug/1947791"
    jt1 = Article(url)

    jt1.download()
    jt1.parse()
    nltk.download('punkt')
    jt1.nlp()


    # The star
    url = 'https://www.thestar.com.my/news/nation/2021/02/07/courier-company-says-sorry-over-039violent-sorting-of-packages039'
    jt2 = Article(url)

    jt2.download()
    jt2.parse()
    jt2.nlp()


    # the rakyat post
    url = 'https://www.therakyatpost.com/2021/02/07/jt-express-protests-whats-going-on-how-to-claim-your-money-back/'
    jt3 = Article(url)

    jt3.download()
    jt3.parse()
    jt3.nlp()


    # Pos Laju
    # the rakyat pos
    url = "https://www.therakyatpost.com/2020/05/19/why-are-our-abang-pos-laju-not-getting-raya-bonuses/"
    pl1 = Article(url)

    pl1.download()
    pl1.parse()
    pl1.nlp()


    # the rakyat pos
    url = "https://www.theedgemarkets.com/article/kitchen-sinking-drags-pos-malaysia-its-largest-quarterly-net-loss"
    pl2 = Article(url)

    pl2.download()
    pl2.parse()
    pl2.nlp()


    # the star
    url = "https://www.thestar.com.my/news/nation/2020/09/08/pos-malaysias-sendparcel-to-hit-record-breaking-two-million-parcels-monthly"
    pl3 = Article(url)

    pl3.download()
    pl3.parse()
    pl3.nlp()


    # GDEX
    # the edge market
    url = "https://www.theedgemarkets.com/article/gdex-looks-regional-markets-local-competition-heats"
    gd1 = Article(url)

    gd1.download()
    gd1.parse()
    gd1.nlp()


    # the star
    url = "https://www.thestar.com.my/business/business-news/2021/01/30/digitalisation-a-game-changer-for-gdex"
    gd2 = Article(url)

    gd2.download()
    gd2.parse()
    gd2.nlp()


    # the edge market
    url = "https://www.theedgemarkets.com/article/gdex-partners-tasco-improve-logistics-delivery-services"
    gd3 = Article(url)

    gd3.download()
    gd3.parse()
    gd3.nlp()


    # DHL
    # the rakyat pos
    url = "https://www.therakyatpost.com/2019/06/04/unclaimed-dhl-mystery-packages-auctioned-at-ramadan-bazaar/"
    dhl1 = Article(url)

    dhl1.download()
    dhl1.parse()
    dhl1.nlp()


    # malay mail
    url = "http://malaymail.com/news/money/2021/04/08/maskargo-eyes-higher-market-share-with-new-service/1964818"
    dhl2 = Article(url)

    dhl2.download()
    dhl2.parse()
    dhl2.nlp()


    # The star
    url = 'https://www.thestar.com.my/business/business-news/2017/11/23/dhl-to-invest-rm1pt5b-more-in-cyberjaya-it-services-data-centre'
    dhl3 = Article(url)

    dhl3.download()
    dhl3.parse()
    dhl3.nlp()



    # City Link Express
    # The star
    url = "https://www.thestar.com.my/business/business-news/2020/10/27/freeze-on-courier-licences-for-two-years"
    cle1 = Article(url)

    cle1.download()
    cle1.parse()
    cle1.nlp()


    # malay mail
    url = "https://www.malaymail.com/news/malaysia/2020/10/26/with-109-courier-firms-in-malaysia-mcmc-suspends-new-licence-issuance-until/1916342"
    cle2 = Article(url)

    cle2.download()
    cle2.parse()
    cle2.nlp()


    # auto world
    url = 'http://autoworld.com.my/news/2020/09/25/city-link-express-takes-delivery-of-277-new-isuzu-trucks/'
    cle3 = Article(url)

    cle3.download()
    cle3.parse()
    cle3.nlp()


    """ Combine the text from sites for each delivery company"""
    cle_text = cle1.text + cle2.text + cle3.text
    pl_text = pl1.text + pl2.text + pl3.text
    gd_text = gd1.text + gd2.text + gd3.text
    jt_text = jt1.text + jt2.text + jt3.text
    dhl_text = dhl1.text + dhl2.text + dhl3.text

    """ Save to text file """
    text_file = open("../News/cle_text.txt", "w", encoding='utf-8')
    text_file.write(cle_text)
    text_file.close()
    text_file = open("../News/pl_text.txt", "w", encoding='utf-8')
    text_file.write(pl_text)
    text_file.close()
    text_file = open("../News/gd_text.txt", "w", encoding='utf-8')
    text_file.write(gd_text)
    text_file.close()
    text_file = open("../News/jt_text.txt", "w", encoding='utf-8')
    text_file.write(jt_text)
    text_file.close()
    text_file = open("../News/dhl_text.txt", "w", encoding='utf-8')
    text_file.write(dhl_text)
    text_file.close()

"""
findAndDeleteStopWords find and delete stop words in articles, 
return an array of size 5 containing stop words count for each company 
"""
def findAndDeleteStopWords():
    stopwords_trie = trie()
    stopwords_count = []

    with open("../Misc/stopwords.txt") as file_in:
        for word in file_in:
            stopwords_trie.insert(word.strip())

    for idx in range(len(delivery_list)):
        list_ = []
        stopwords = 0

        # Open the article file
        with open("../News/" + delivery_list[idx], encoding='utf-8') as f:
                list_ = f.readlines()

        # Remove unnecessary new lines
        for i in range(len(list_)):
            list_[i] = list_[i].strip()
            list_[i] = re.sub("[^a-zA-Z0-9\s]+", "", list_[i])
        list_ = list(filter(None, list_))

        # Count, find and delete stopwords
        for i in range(len(list_)):
            temp_str = ""
            temp_arr = list_[i].split(sep=' ')
            for word in temp_arr:
                if stopwords_trie.search(word):
                    stopwords += 1
                else:
                    temp_str += word + " "
            temp_str = temp_str.rstrip()
            list_[i] = temp_str

        # add the stopword count to the result array
        stopwords_count.append(stopwords)

        # Write the cleaned version to text file
        with open("../News/Cleaned/" + delivery_list[idx], "w", encoding='utf-8') as f:
            for line in list_:
                f.write("%s\n" % line)

    return stopwords_count

""" 
countWordTypes
Prepare the dictionary for positve and negative words
Return an array of size 5, each element is a list of 3 dictionary, storing positive, negative, and neutral words-frequency
"""
def countWordTypes():
    # Use trie to store all the positive and negative words
    positive_trie = trie()
    negative_trie = trie()

    # pos is an array of string, where each string contains words starting with alphabet a - z
    pos = [
        'A REASON FOR BEING,  ABLE,  ABOUND,  ABOUNDING,  ABOUNDS,  ABRACADABRA,  ABSOLUTE,  ABSOLUTELY,  ABSORBED,  ABUNDANCE,  ABUNDANT,  ABUNDANT GRATIFICATION,  ACARONAR,  ACCENTUACTIVITY,  ACCEPT,  ACCEPTABLE,  ACCEPTANCE,  ACCEPTED,  ACCEPTING, ACCESSIBLE,  ACCLAIM,  ACCLAIMED,  ACCLAMATION,  ACCOLADE,  ACCOMMODATE,  ACCOMMODATED,  ACCOMMODATING,  ACCOMMODATION,  ACCOMMODATIVE,  ACCOMPLISH,  ACCOMPLISHED,  ACCOMPLISHMENT,  ACCOMPLISHMENTS,  ACCOUNTABILITY,  ACCURACY,  ACCURATE,  ACCURATELY,  ACHIEVABLE,  ACHIEVE,  ACHIEVEMENT,  ACHIEVEMENTS,  ACKNOWLEDGMENT,  ACTABILITY,  ACTION,  ACTION FOR HAPPINESS,  ACTIVATE,  ACTIVE,  ACTIVE AND CONSTRUCTIVE STEPS,  ACTS OF KINDNESS,  ACUMEN,  ADAPTABILITY,  ADAPTABLE,  ADAPTIVE,  ADD,  ADDITION,  ADEQUATE,  ADJUSTABLE,  ADMIRABLE,  ADMIRABLY,  ADMIRATION,  ADMIRE,  ADMIRED,  ADMIRER,  ADMIRING,  ADMIRINGLY,  ADORABLE,  ADORE,  ADORED,  ADORER,  ADORING,  ADORINGLY,  ADROIT,  ADROITLY,  ADULATED,  ADULATION,  ADULATORY,  ADVANCED,  ADVANTAGE,  ADVANTAGEOUS,  ADVANTAGEOUSLY,  ADVANTAGES,  ADVENTURE,  ADVENTURESOME,  ADVENTUROUS,  ADVOCATED,  AFFABILITY,  AFFABLE,  AFFABLY,  AFFECTION,  AFFECTIONATE,  AFFINITY,  AFFIRM,  AFFIRMATION,  AFFIRMATIVE,  AFFLUENCE,  AFFLUENT,  AFFORD,  AFFORDABLE,  AFFORDABLY,  AGELESS,  AGILE,  AGILELY,  AGILITY,  AGREE,  AGREEABLE,  AGREEABLENESS,  AGREEABLY,  AID,  AIM,  AIR,  AIRNESS,  AKASHIC RECORDS,  ALACRITY,  ALERT,  ALERTNESS,  ALIGNED,  ALIVE,  ALIVENESS,  ALL IS WELL,  ALLOW,  ALLOWING,  ALLURE,  ALLURING,  ALLURINGLY,  ALOHA,  ALTERNATIVE HEALING,  ALTITUDINARIAN,  ALTRUCAUSE,  ALTRUISM,  ALTRUISTIC,  ALTRUISTICALLY,  AMAZE,  AMAZED,  AMAZEMENT,  AMAZES,  AMAZING,  AMAZING WORDS,  AMAZINGLY,  AMBITION,  AMBITIOUS,  AMBITIOUSLY,  AMELIORATE,  AMENITY,  AMIABILITY,  AMIABLE,  AMIABLY,  AMICABILITY,  AMICABLE,  AMICABLY,  AMIN,  AMITY,  AMPLE,  AMPLY,  AMUSE,  AMUSED,  AMUSING,  AMUSINGLY,  ANGEL,  ANGELIC,  ANIMATE,  ANIMATED,  ANIMATENESS,  ANIMATING,  ANIMATION,  ANTICIPATION,  APOTHEOSIS,  APPEAL,  APPEALING,  APPLAUD,  APPRECIABLE,  APPRECIATE,  APPRECIATED,  APPRECIATES,  APPRECIATION,  APPRECIATION OF BEAUTY,  APPRECIATIVE,  APPRECIATIVE JOY,  APPRECIATIVELY,  APPRECIATIVENESS,  APPROPRIATE,  APPROVAL,  APPROVE,  ARDENT,  ARDOR,  AROUSED,  ART OF APPRECIATION,  ART OF STILLNESS,  ART OF WELLBEING,  ASSERTIVE,  ASSERTIVENESS,  ASSUME YOUR OWN VALUE,  ASSURANCE,  ASTONISHED,  ASTONISHING,  ASTONISHINGLY,  ASTONISHMENT,  ASTOUNDING,  ASTRONOMICAL,  ATTENTIVENESS,  ATTRACTION,  ATTRACTIVE,  ATTRIBUTIONAL STYLE QUESTIONNAIRE (ASQ),  AUDACITY,  AURORA,  AUTHENTIC,  AUTHENTIC HAPPINESS,  AUTHENTICITY,  AWAKENING,  AWARE,  AWARENESS,  AWE,  AWED,  AWE-GASMIC,  AWESOME,  AWESOMENESS',
        'BADASSERY,  BALANCE,  BALANCED,  BALLISTIC,  BE EXTRAORDINARY,  BE HAPPY,  BEATIFY,  BEATITUDE,  BEAUTIFUL ,  BEAUTIFULLY,  BEAUTIFY,  BEAUTY,  BEAUTY IN ALL THINGS,  BEING AT REST,  BEINGNESS,  BELIEVABLE,  BELONG,  BELONGING,  BELOVED,  BENEFACTOR,  BENEFICIAL,  BENEFIT,  BENEFITS,  BENEVOLENCE,  BENEVOLENT,  BENEVOLENTLY,  BENEVOLENTLY CHEERFUL STATE OF MIND,  BEST,  BEST OF ALL POSSIBLE WORLDS,  BEST-SELLING,  BETTER,  BETTER AND BETTER,  BETTER-KNOWN,  BETTER-THAN-EXPECTED,  BEYOND,  BEYOND FABULOUS,  BEYOND THANK YOU,  BIG VISION,  BIOPHILIA,  BLASTING,  BLASTING LOVE,  BLAZING,  BLESS,  BLESSED,  BLESSING,  BLINDING,  BLING BLING,  BLISS,  BLISS ON TAP,  BLISSCIPLINE,  BLISSFUL,  BLISSFULNESS,  BLITHESOME,  BLOOD-BROTHERS,  BLOOM,  BLOSSOM,  BLOSSOMING,  BOHEMIAN SOUL,  BOHO-SOUL,  BOLDNESS,  BONUS,  BRAVERY,  BREATHTAKING,  BREEZINESS,  BRIGHT,  BRIGHTEN,  BRIGHTNESS,  BRILLIANCE,  BRILLIANT,  BRIO,  BRISKNESS,  BUBBLING,  BUDDHAHOOD,  BUDO,  BULLISHNESS,  BUOYANCY,  BUSTING',
        'CALM,  CANDOR,  CAPABILITY,  CAPABLE,  CAPABLY,  CAPITAL,  CARE,  CAREFREE,  CAREFREENESS,  CAREFULNESS,  CARESS,  CARING,  CELEBRATE,  CELEBRATION,  CENTERED,  CENTERING,  CENTERING MEDITATION,  CEREBRO,  CERTAIN ,  CERTAINTY,  CHAKRA,  CHALLENGE,  CHAMPION,  CHANGE,  CHARISMA,  CHARISMATIC,  CHARITABLE,  CHARITY,  CHARM,  CHARMER,  CHARMING,  CHEERFUL,  CHEERFUL MOOD,  CHEERFUL WILLINGNESS,  CHEERFULNESS,  CHEERS,  CHI,  CHOICE,  CITIZEN OF MASTERY,  CLARITY,  CLASSY,  CLEAN,  CLEANLINESS,  CLEAR,  CLEAR HEADED,  CLOSENESS,  CO-CREATING,  CO-CREATOR,  COHESION,  COLLABORATION,  COLLECTED,  COMFORT,  COMFORTABLE,  COMFORTING,  COMMITMENT,  COMMUNICATION,  COMMUNION,  COMMUNITY,  COMPANIONSHIP,  COMPASSION,  COMPASSIONATE,  COMPETENCE,  COMPETENCY,  COMPETENT,  COMPLIMENTARY WORDS,  COMPOSURE,  CONCENTRATION,  CONCORD,  CONFIDENCE,  CONFIDENT,  CONGRUENCE,  CONNECT,  CONNECTED,  CONNECTEDNESS,  CONNECTION,  CONQUER,  CONSCIOUSNESS,  CONSCIOUSNESS ENGINEERING,  CONSIDERATE,  CONSIDERATION,  CONSISTENCY,  CONSISTENT,  CONTENT,  CONTENTED,  CONTENTMENT,  CONTINUAL STREAM OF SYNCHRONICITY,  CONTINUITY,  CONTINUOUS,  CONTRIBUTION,  CONVICTION,  CONVINCING,  COOL,  COOPERATION,  COPACABANA,  CORDIAL,  CORKING,  COSMIC AWARENESS,  COURAGE,  COURTEOUS,  COURTESY,  COZINESS,  CRANK (UP),  CREATE,  CREATIVE,  CREATIVE AFFIRMATIONS,  CREATIVE PROCESS,  CREATIVENESS,  CREATIVITY,  CUDDLE,  CUDDLING,  CURIOSITY,  CURIOUS,  CUTE,  CUTENESS',
        'DAIMON,  DANDY,  DARING,  DAUWTRAPPEN,  DAZZLE,  DAZZLED,  DEBONAIR,  DECENT,  DECISIVENESS,  DEDICATED,  DEEPER PART OF YOU,  DEFENCELESSNESS,  DELICATE,  DELICIOUS,  DELICIOUSNESS,  DELIGHT,  DELIGHTED,  DELIGHTFUL,  DELIGHTFULLY,  DEPENDABILITY,  DESERVE,  DESERVEDNESS,  DESERVINGNESS,  DESIRABLE,  DESIRE,  DETACHMENT,  DETERMINATION,  DEVOTED,  DEVOTION,  DIGNITY,  DILIGENCE,  DIRECTION,  DISCIPLINE,  DISCOVERY,  DISCRETION,  DIS-IDENTIFY,  DISNEY,  DIVERSITY,  DIVINE,  DO,  DOPE,  DOPE CHILL OUT,  DREAM,  DREAMY,  DRIVE,  DUTY,  DYNAMIC',
        'E MA HO,  EAGER,  EAGERNESS,  EARNEST,  EARTHING,  EASE,  EASE-OF-MIND,  EASIER,  EASILY,  EASY,  EASY TO APPROACH,  EASY TO TALK TO,  EBULLIENCE,  ECOSOPHY,  ECSTATIC,  ECSTATIFY,  EDUCATE,  EDUCATED,  EDUCATION,  EFFECTIVENESS,  EFFICACY,  EFFICIENCY,  EFFICIENT,  EFFORTLESS EASE,  EFFORTLESSLY,  EFFORTLESSNESS,  EKAGGATA,  ELATED,  ELATION,  ELECTRIC,  ELEGANCE,  ELEVATE,  ELEVATED,  EMBODY THE LOVE,  EMBRACE,  EMPATHIZE,  EMPATHY,  EMPHATIC,  EMPOWER,  EMPOWERED,  EMPOWERING,  EMPOWERING WORDS,  EMULATE,  ENABLE,  ENABLED,  ENCHANTED,  ENCOURAGE,  ENCOURAGED,  ENCOURAGEMENT,  ENCOURAGING WORDS,  ENDLESS,  ENDURANCE,  ENERGETIC,  ENERGIZE,  ENERGY,  ENGAGE,  ENGAGED,  ENGAGING,  ENGROSSED,  ENJOY,  ENJOYMENT,  ENLIGHTENED,  ENLIGHTENMENT,  ENLIVENED,  ENORMOUS,  ENOUGH,  ENTHRALLED,  ENTHUSIASM,  ENTHUSIASTIC,  ENTRANCED,  EQUALITY,  EQUANIMITY,  EQUANIMOUS,  EQUITABLE,  EQUITABLY,  EQUITY,  ERLEBNIS,  ETERNAL,  ETHEREAL,  EUDAEMONISM,  EUDAEMONIST,  EUDAEMONISTIC,  EUDAIMONIA,  EUDAMONIA,  EUNOIA,  EVER-JOYOUS,  EVER-JOYOUS NOW,  EVOLVE,  EXALTATION,  EXALTING,  EXCELLENCE,  EXCELLENT,  EXCEPTIONAL,  EXCITE,  EXCITED,  EXCITED ANTICIPATION,  EXCITEMENT,  EXCITING,  EXEMPLARY,  EXHILARATING,  EXPANSIVE,  EXPECTANT,  EXPERIENCE,  EXPERTISE,  EXPLORATION,  EXPRESSING,  EXPRESSIVENESS,  EXQUISITE,  EXSTATISFY,  EXTRA,  EXTRAORDINARY,  EXUBERANCE,  EXUBERANT,  EXULTANT',
        'FABULOUS,  FAIR,  FAIRNESS,  FAITH,  FAITHFUL,  FAME,  FAMILY,  FAMOUS,  FANCY,  FANTABULOUS,  FANTASTIC,  FASCINATE,  FASCINATED,  FAVORITE,  FEARLESS,  FEASIBLE,  FEEL GOOD,  FEELING GOOD,  FEISTINESS,  FEISTY,  FELICITY,  FESTIVE,  FESTIVENESS,  FIDELITY,  FINE,  FIT,  FLASHY,  FLAUNTING,  FLAWLESS,  FLAWLESSLY,  FLEXIBILITY,  FLOURISH,  FLOURISHING,  FLOW,  FLOWING,  FOCUS,  FONDLE,  FOOD,  FORGIVE,  FORGIVENESS,  FORGIVING,  FORTITUDE,  FORTUITOUS,  FREE,  FREECYCLE,  FREEDOM,  FREE-SPIRITED,  FRIC-TIONLESSLY,  FRIEND,  FRIENDLINESS,  FRIENDLY,  FRIENDSHIP,  FRUGALITY,  FTW,  FULFILL,  FULFILLED,  FUN,  FUNERIFIC,  FUN-LOVING,  FUNNY JOKES,  FUNOLOGY,  FUTURE',
        'GAME-CHANGER,  GARGANTUAN,  GEMUTLICHKEIT,  GENERATE,  GENERATOR OF LIFE,  GENERAVITY,  GENEROSITY,  GENEROUS,  GENIAL,  GENIUS,  GENTLEMAN,  GENUINE,  GENUINENESS,  GIBIGIANA,  GIDDY,  GIFT,  GIGGLING,  GIGIL,  GINGER,  GIVE,  GIVING,  GLAD,  GLAMOR,  GLORY,  GLOW,  GOD,  GODDESS,  GODLINESS,  GOING THE EXTRA MILE,  GOLDILOCKS,  GOOD,  GOOD DONE IN SECRET,  GOOD FORTUNE,  GOOD HEALTH,  GOOD INDWELLING SPIRIT,  GOOD WORD,  GOOD WORDS,  GOOD-FEELING,  GOOD-HUMORED,  GOODNESS,  GOODWILL,  GORGEOUS,  GORGEOUSNESS,  GRACE,  GRACEFULLY,  GRACIOUSNESS,  GRAND,  GRANDIOSITY,  GRATEFULNESS,  GRATITUDE,  GREAT,  GREAT ZEAL,  GREATFUL,  GROOVY,  GROUNDED,  GROW,  GROWTH,  GUIDANCE,  GUIDE,  GUIDING,  GYPSY SOUL',
        'HABITUATION,  HAKUNA MATATA,  HALCYON,  HALL OF AWESOMENESS,  HALO,  HANDSOME,  HAPPILY,  HAPPINESS,  HAPPY,  HAPPY HEARTED,  HAPPY WORDS,  HARMONIOUS,  HARMONIZE,  HARMONY,  HARNESS,  HEALTH,  HEALTHY,  HEART,  HEARTFELT,  HEART-OPENING,  HEARTWARMING,  HEAVEN,  HEAVENLY,  HEEDFUL,  HEIGHTENED,  HELLO,  HELP,  HELPFUL,  HELPFULNESS,  HELPING,  HERO,  HEROISM,  HIGHER CONSCIOUSNESS,  HIGHLY DISTINGUISHED,  HIGH-SPIRITEDNESS,  HOLINESS,  HOLISTIC,  HOLY,  HOLY SPIRIT,  HONEST,  HONESTY,  HONEY BADGER,  HONOR,  HOPE,  HOPEFULNESS,  HOSPITABLE,  HOSPITALITY,  HOT,  HUGE,  HUMAN,  HUMAN FLOURISHING,  HUMBLE,  HUMOR',
        'ICHARIBA CHODE,  IDEA,  IDEALISM,  IKIGAI,  ILLUMINATED,  ILLUMINATION,  ILLUSTRIOUS,  IMAGINATION,  IMPROVEMENT,  INCLUSION,  INCLUSIVENESS,  INCOMPARABLE,  INCREDIBLE,  INCREDIBLE CUTENESS,  INDEPENDENCE,  INDWELLING,  INEFFABILITY,  INEFFABLE,  INFINITE,  INFINITY,  INFLUENCE,  INGENUITY,  IN-LOVE,  INNER,  INNER PEACE,  INNER SPIRIT,  INNOCENT,  INNOVATE,  INNOVATION,  INQUISITIVE,  INSIGHT,  INSIGHTFUL,  INSIGHTFULNESS,  INSPIRATION,  INSPIRATIONAL,  INSPIRATIONAL WORDS,  INSPIRE,  INSPIRED,  INSPIRING WORD,  INSPIRING WORDS,  INTEGRITY,  INTELLIGENCE,  INTELLIGENT,  INTENSITY,  INTENTION,  INTERCONNECTED,  INTERCONNECTIVITY,  INTEREST,  INTERESTED,  INTERESTING,  INTIMACY,  INTREPID,  INTRIGUED,  INTUITION,  INTUITIVENESS,  INVENTIVENESS,  INVESTING,  INVIGORATE,  INVIGORATED,  INVINCIBLE,  INVOLVE,  INVOLVED,  IRIDESCENT',
        'JAMMIN,  JOKE,  JOLLY,  JOVIAL,  JOY,  JOYFUL,  JOYOUS,  JUBILANT,  JUBILINGO,  JUMPY,  JUST,  JUSTICE,  JUVENESCENT',
        'KAAJHUAB,  KALEIDOSCOPES OF BUTTERFLIES,  KALON,  KEEN,  KEEP-UP,  KI,  KILIG,  KIND,  KIND WORDS,  KIND-HEART,  KINDLY,  KINDNESS,  KISS,  KITTENS,  KNOWLEDGE,  KOIBITO KIBUN',
        'LAUGH,  LAUGHING,  LEADER,  LEADERSHIP,  LEADING,  LEARN,  LEARNING,  LEEWAY,  LET GO,  LETTING GO,  LIBERTY,  LIFE,  LIFE OF THE PARTY,  LIGHT,  LIGHT FOG,  LIGHT-HEARTED,  LIGHTWORKER,  LIKE,  LIVE,  LIVELINESS,  LIVELY,  LIVES THROUGH,  LIVING,  LOGIC,  LONGEVITY,  LOVABLE,  LOVE,  LOVE FULFILLED,  LOVE WORDS,  LOVELY,  LOVER OF BEAUTY,  LOVING,  LOVING ACCEPTANCE,  LOVING ATTENTION,  LOVING FEELINGS,  LOVING-KINDNESS,  LOYAL,  LOYALTY,  LUCK,  LUCKY,  LUSTROUS,  LUSTROUS COLORS,  LUXURY',
        'MAGIC,  MAGNETIC TO LOVE,  MAGNIFICENT,  MAJESTY,  MAJOR,  MAKING A DIFFERENCE,  MANY,  MARVELOUS,  MASTERY,  MATURITY,  MEANING,  MEANINGFUL,  MEANINGFUL WORDS,  MEDITATION,  MELIORISM,  MELLOW,  MEMORABLE,  MENCH,  MERCY,  MERIT,  MILD,  MIND-BLOWING,  MINDFUL,  MINDFULNESS,  MINDSIGHT,  MIRACLE,  MIRTHFUL,  MODESTY,  MOJO,  MORE,  MORPHING,  MOTIVATE,  MOTIVATED WORDS,  MOTIVATING WORDS,  MOTIVATION,  MOTIVATIONAL,  MOTIVATIONAL WORDS,  MOURNING,  MOVED,  MOVEMENT,  MOVING,  MUTUALITY,  MYRIAD',
        'NAMASTE,  NATURE-MADE,  NEAT,  NEOTENY,  NEW,  NICE,  NICE WORDS,  NIRVANA,  NOBLE,  NON-DUALITY,  NON-RESISTANCE,  NON-RESISTANT,  NOURISH,  NOURISHED,  NOURISHING,  NOURISHMENT,  NOVATURIENT,  NURTURE,  NURTURING',
        'OBEDIENT,  OK,  OKAGE SAMA,  OM MANI PADME HUM,  OMG,  OMNISCIENCE,  ON,  ONENESS,  ONE-POINTEDNESS,  ONEUP,  ONWARDS,  OPEN,  OPEN HEARTED,  OPENING,  OPENLY,  OPEN-MINDED,  OPENNESS,  OPPORTUNITY,  OPTIMISM,  OPTIMIST,  OPTIMISTIC,  ORDER,  ORENDA,  ORGANIZATION,  ORIENTATION,  ORIGINAL,  ORIGINALITY,  OUTCOME,  OUTERNATIONALIST,  OUTGOING,  OUTSTANDING,  OVERCOME,  OVERLY OPTIMISTIC,  OWNING YOUR POWER',
        'PACIFY,  PANACHE,  PARADISE,  PARADISIAC,  PARDON,  PARTICIPATION,  PASSION,  PASSIONATE,  PATIENCE,  PEACE,  PEACE OF MIND,  PEACEFUL WORDS,  PEP,  PEPPINESS,  PERCEPTIVENESS,  PERFECT,  PERFECTION,  PERKINESS,  PERMALICIOUS,  PERSEVERANCE,  PERSISTENCE,  PERSONAL GROWTH,  PETRICHOR,  PHILOCALIST,  PICK-ME-UP,  PICTURESQUE,  PIOUS,  PIQUANCY,  PLAY,  PLAYFUL,  PLAYFULNESS,  PLEASE,  PLEASED,  PLEASURE,  PLUCKY,  POLITE,  POLITENESS,  POLLYANNAISM,  POSICHOICE,  POSIDRIVING,  POSIFIT,  POSILENZ,  POSIMASS,  POSIMINDER,  POSIRATIO,  POSIRIPPLE,  POSIRIPPLER,  POSIRIPPLES,  POSISINGER,  POSISITE,  POSISTRENGTH,  POSITIBILITARIAN,  POSITIVE ADJECTIVES,  POSITIVE ATTITUDE,  POSITIVE BELIEFS,  POSITIVE CIRCUMSTANCES,  POSITIVE EMOTIONS,  POSITIVE ENERGY,  POSITIVE EVENTS,  POSITIVE FEELINGS,  POSITIVE MIND,  POSITIVE THESAURUS,  POSITIVE THINKING,  POSITIVE THOUGHTS,  POSITIVE VOCABULARY,  POSITIVE WORDS,  POSITRACTION,  POSITUDE,  POSIVALUES,  POSIWORD,  POSSIBILITARIAN,  POUR YOUR LOVE,  POWER,  POWER WORDS,  POWERFUL,  POWERFUL POSITIVE WORDS,  POWERFUL POSSIBILITY,  POWERFUL WORDS,  POWER-ON,  POWER-UP,  PRACTICALITY,  PRANA,  PRECIOUS,  PRECISION,  PREPAREDNESS,  PRESENCE,  PRESERVATION,  PRETTY,  PRICELESS,  PRIDE,  PRIVACY,  PRIVILEGE,  PROACTIVE,  PROACTIVITY,  PROGRESS,  PROMPTNESS,  PRONIA,  PROPITIOUS,  PROSPERITY,  PROSPEROUS,  PROTECT,  PROTO,  PROUD,  PUNCTUAL,  PUNCTUALITY,  PUPPIES,  PURE,  PURPOSE',
        'QUAINT,  QUALITY,  QUALITY WORDS,  QUANTUM CONSCIOUSNESS,  QUANTUMNESS,  QUEENLY,  QUICKENING,  QUIDDITY,  QUIESCENT,  QUIESCENT MIND,  QUIET,  QUIETNESS',
        'RADIANT,  RADIATE,  RAINBOW,  RAPTURE,  RAPTUROUS,  RASASVADA,  RATIONALITY,  READINESS,  READY,  REAL,  REALITY,  REASON,  REBORN,  RECOGNITION,  RECOGNIZE,  RECOMMEND,  REFRESH,  REFRESHED,  REJUVENATE,  REJUVENATED,  RELATEDNESS,  RELATIONSHIPS,  RELAX,  RELAXED,  RELEASING,  RELENT,  RELIABILITY,  RELIABLE,  RELIEF,  RELIEVE,  RELIEVED,  RELIGION,  REMARKABLE,  RENEW,  RENEWED,  RENOWNED,  REPOSE,  RESILIENCE,  RESILIENT,  RESOURCEFULNESS,  RESPECT,  RESPECTED,  RESPONSIBILITY,  REST,  RESTED,  RESTORE,  RESTORED,  REVELATION,  REVERENCE,  REVIVED,  RIGHTEOUSNESS,  RIGHTFUL,  RIPE,  RISK-TAKING,  ROCKSTAR,  ROMANCE,  ROMANTIC,  ROSINESS',
        'SACRED,  SACRED SPACE,  SAFE,  SAFETY,  SALVATION,  SASSY,  SATISFIED,  SAVE,  SAVINGS,  SAVOUR,  SAVOURING,  SCOPE,  SECURE,  SECURED,  SECURITY,  SELF-COMPASSION,  SELF-ESTEEM,  SELF-EXPRESSION,  SELF-FORGIVENESS,  SELF-KINDNESS,  SELFLESSNESS,  SELF-LOVE,  SELF-RESPECT,  SERENDIPITY,  SERENE,  SERENITY,  SERVE,  SERVICE,  SHAPE-SHIFTING VIRTUOSO,  SHELTER,  SHIFT IN FOCUS,  SHINE,  SHINING,  SHOW UP MORE PRESENT,  SIMPLE,  SIMPLICITY,  SIMPLIFY,  SINCERITY,  SKILL,  SKILLED,  SLAYING YOUR DRAGON,  SLEEP,  SMART,  SMILE,  SMILING,  SOUL,  SOULFUL,  SOULMATE,  SOUL-STRETCHING,  SPACE,  SPACIOUS,  SPARK,  SPARKLE,  SPARKLES,  SPECIAL,  SPECTACULAR,  SPELLBOUND,  SPIRIT,  SPLENDID,  SPONTANEITY,  SPONTANEOUS,  SPUNKY,  STABILITY,  START,  STEADFASTNESS,  STELLAR,  STILL,  STIMULATED,  STIMULATING,  STIMULATION,  STRENGTH,  STRIVE,  STRONG WORDS,  STUDIOUS,  STUDY,  STUPENDOUS,  STYLE,  SUBLIME,  SUCCULENT,  SUFFICIENT,  SUNNINESS,  SUNSHINE,  SUPERCALIFRAGILISTIC,  SUPERCALIFRAGILISTICEXPIALIDOCIOUS,  SUPERCHARGE,  SUPERCHARGED,  SUPERPOWER,  SUPPORT,  SUPPORTED,  SUPPORTING,  SUPREME,  SURPRISED,  SUSTAIN,  SUSTAINED,  SWAG,  SWAGGY,  SWEET,  SWEETHEART,  SWEETNESS,  SYMPATHETIC,  SYMPTOMS OF GREATNESS,  SYNCHRONICITY,  SYNERGY,  SYSTEMATIZATION',
        'TACT,  TEACH,  TEACHABLE,  TEAM,  TEAMWORK,  TEMUL,  TENACITY,  TENDER,  TENDERLY,  THANK,  THANKFUL,  THANKFUL,  THANKFULNESS,  THANK-YOU ,  THE GREAT SPIRIT,  THERAPY,  THRILLED,  THRIVE,  THRIVING,  TICKLED,  TIDSOPTIMIST,  TIME,  TIME OPTIMIST,  TIMELINESS,  TO BE,  TO BE KNOWN,  TO BE SEEN,  TO KNOW,  TO LET GO,  TO MATTER,  TOLERANCE,  TOUCH,  TOUCHED,  TRADITION,  TRANQUIL,  TRANQUILITY,  TRANSFORM,  TRANSFORMATION,  TRANSFORMATIVE,  TRANSPARENT,  TRIUMPH,  TRUST,  TRUSTING,  TRUTH,  TRUTHFULNESS',
        'UBUNTU,  ULTIMATE,  UNABASHED,  UNABASHED PLEASURE,  UNBEARABLY CUTE,  UNBELIEVABLE,  UNCONDITIONAL,  UNDERSTAND,  UNDERSTANDING,  UNDERSTOOD,  UNFLAPPABLE,  UNHURRY,  UNIFICATION,  UNIFICATION OF MIND,  UNIQUE,  UNITY,  UNREAL,  UP,  UPGRADE,  UP-LEVELED,  UPLIFT,  UPSKILL,  USEFUL,  USER-FRIENDLY,  UTTER AMAZEMENT',
        'VALID,  VALUABLE,  VALUE,  VALUES,  VARIETY,  VENERATION,  VERIFY,  VERSATILITY,  VERY,  VIABLE,  VIBRANT,  VICTORIOUS,  VICTORY,  VIGOR,  VIM,  VIRTUE,  VIRTUOUS,  VITALITY,  VOCABULEVERAGE,  VOW,  VULNERABILITY,  VULNERABLE',
        'WALWALUN,  WANDERLUST,  WARM,  WARMTH,  WATER,  WEALTH,  WEB OF RELATEDNESS,  WELCOME,  WELFARE,  WELL,  WELL-BEING,  WELLNESS,  WHOLE,  WHOLEHEARTEDLY,  WHOLEHEARTEDNESS,  WILL,  WILLING,  WILLING TO LEARN,  WILLINGNESS,  WIN,  WINNABLE,  WINNING,  WISDOM,  WISE,  WON,  WONDER,  WONDERFUL,  WONDER-WORKING,  WONDROUS,  WORLD-BUILDER,  WORTH,  WORTHINESS,  WORTHINESS TO TAKE UP SPACE,  WORTHY,  WOW',
        'XENIAL,  XENODOCHIAL,  XENOPHILE,  XFACTOR,  XO,  X-RAY VISION',
        'YARAANA,  YAY,  YEA,  YEAH,  YEARN,  YEN,  YES,  YESABILITY,  YESABLE,  YIPPEE,  YOU ARE LOVED,  YOUNG,  YOUNG-AT-HEART,  YOUR TRUE VALUE,  YOUTH,  YOUTHFUL,  YUGEN,  YUMMY',
        'ZAJEBISCIE,  ZANY,  ZAPPY,  ZEAL,  ZEALOUS,  ZEST,  ZEST FOR LIFE,  ZESTFUL,  ZESTY,  ZING,  ZIPPY']
    # extract each word
    pos_list = [x.lower().split(sep=',  ') for x in pos]
    for line in pos_list:
        for word in line:
            word = re.sub("[^a-zA-Z0-9\s]+", "", word)
            positive_trie.insert(word)


    # neg is an array of string, where each string contains words starting with alphabet a - z
    neg = [
        'abnormal,    abolish,    abominable,    abominably,    abominate,    abomination,    abort,    aborted,    aborts,    abrade,    abrasive,    abrupt,    abruptly,    abscond,    absence,    absent-minded,    absentee,    absurd,    absurdity,    absurdly,    absurdness,    abuse,    abused,    abuses,    abusive,    abysmal,    abysmally,    abyss,    accidental,    accost,    accursed,    accusation,    accusations,    accuse,    accuses,    accusing,    accusingly,    acerbate,    acerbic,    acerbically,    ache,    ached,    aches,    aching,    acrid,    acridly,    acridness,    acrimonious,    acrimoniously,    acrimony,    adamant,    adamantly,    addict,    addicted,    addicting,    addicts,    admonish,    admonisher,    admonishingly,    admonishment,    admonition,    adulterate,    adulterated,    adulteration,    adversarial,    adversary,    adverse,    adversity,    afflict,    affliction,    afflictive,    affront,    afraid,    aggravate,    aggravating,    aggravation,    aggression,    aggressive,    aggressiveness,    aggressor,    aggrieve,    aggrieved,    aghast,    agonies,    agonize,    agonizing,    agonizingly,    agony,    aground,    ail,    ailing,    ailment,    aimless,    alarm,    alarmed,    alarming,    alarmingly,    alienate,    alienated,    alienation,    allegation,    allegations,    allege,    allergic,    allergies,    allergy,    aloof,    altercation,    ambiguity,    ambiguous,    ambivalence,    ambivalent,    ambush,    amiss,    amputate,    anarchism,    anarchist,    anarchistic,    anarchy,    anemic,    anger,    angrily,    angriness,    angry,    anguish,    animosity,    annihilate,    annihilation,    annoy,    annoyance,    annoyances,    annoyed,    annoying,    annoyingly,    annoys,    anomalous,    anomaly,    antagonism,    antagonist,    antagonistic,    antagonize,    anti-,    anti-occupation,    anti-proliferation,    anti-social,    anti-us,    anti-white,    antipathy,    antiquated,    antithetical,    anxieties,    anxiety,    anxious,    anxiously,    anxiousness,    apathetic,    apathetically,    apathy,    apocalypse,    apocalyptic,    apologist,    apologists,    appall,    appalled,    appalling,    appallingly,    apprehension,    apprehensions,    apprehensive,    apprehensively,    arbitrary,    arcane,    archaic,    arduous,    arduously,    argumentative,    arrogance,    arrogant,    arrogantly,    ashamed,    asinine,    asininely,    askance,    asperse,    aspersion,    aspersions,    assail,    assassin,    assassinate,    assault,    astray,    asunder,    atrocious,    atrocities,    atrocity,    atrophy,    attack,    attacks,    audacious,    audaciously,    audaciousness,    audacity,    austere,    authoritarian,    autocrat,    autocratic,    avalanche,    avarice,    avaricious,    avariciously,    avenge,    averse,    aversion,       awful,    awfully,    awfulness,    awkward,    awkwardness,    ax',
        'babble,    back-logged,    back-wood,    back-woods,    backache,    backaches,     backbite,    backbiting,    backward,    backwardness,       backwoods,    bad,    badly,    baffle,    baffled,    bafflement,    baffling,    bait,    balk,    banal,    bane,    banish,    banishment,    bankrupt,    barbarian,    barbaric,    barbarically,    barbarity,    barbarous,    barbarously,    barren,    baseless,    bash,    bashed,    bashful,    bashing,    battered,    battering,    batty,    bearish,    beastly,    bedlam,    bedlamite,    befoul,    beg,    beggar,    beggarly,    begging,    beguile,    belabor,    belated,    beleaguer,    belie,    belittle,    belittled,    belittling,    bellicose,    belligerence,    belligerent,    belligerently,    bemoan,    bemoaning,    bemused,    bent,    berate,    bereave,    bereavement,    bereft,    berserk,    beseech,    beset,    besiege,    besmirch,    betray,    betrayal,    betrayals,    betrayer,    betraying,    betrays,    bewail,    beware,    bewilder,    bewildered,    bewildering,    bewilderingly,    bewilderment,    bewitch,    bias,    biased,    biases,    bicker,    bickering,    bid-rigging,    bigotries,    bigotry,    biting,    bitingly,    bitter,    bitterly,    bitterness,    bizarre,    blab,    blabber,    blackmail,    blah,    blame,    blameworthy,    bland,    blandish,    blaspheme,    blasphemous,    blasphemy,    blasted,    blatant,    blatantly,    blather,    bleak,    bleakly,    bleakness,    bleed,    bleeding,    bleeds,    blemish,    blind,    blinding,    blindingly,    blindside,    blister,    blistering,    bloated,    blockage,    blockhead,    bloodshed,    bloodthirsty,    bloody,    blotchy,    blow,    blunder,    blundering,    blunders,    blunt,    blur,    blurred,    blurring,    blurry,    blurs,    blurt,    boastful,    boggle,    bogus,    boil,    boiling,    boisterous,    bomb,    bombard,    bombardment,    bombastic,    bondage,    bonkers,    bore,    bored,    boredom,    bores,    boring,    botch,    bother,    bothered,    bothering,    bothers,    bothersome,    bowdlerize,    boycott,    braggart,    bragger,    brainless,    brainwash,    brash,    brashly,    brashness,    brat,    bravado,    brazen,    brazenly,    brazenness,    breach,    break,    break-up,    break-ups,    breakdown,    breaking,    breaks,    breakup,    breakups,    bribery,    brimstone,    bristle,    brittle,    broke,    broken,    broken-hearted,    brood,    browbeat,    bruise,    bruised,    bruises,    bruising,    brusque,    brutal,    brutalities,    brutality,    brutalize,    brutalizing,    brutally,    brute,    brutish,    buckle,    bug,    bugging,    buggy,    bugs,    bulkier,    bulkiness,    bulky,        bull****,    bull—-,    bullies,    bulls..t,    bully,    bullying,    bullyingly,    bum,    bump,    bumped,    bumping,    bumps,    bumpy,    bungle,    bungler,    bungling,    bunk,    burden,    burdensome,    burdensomely,    burn,    burned,    burning,    burns,    bust,    busts,    busybody,    butcher,    butchery,    buzzing,    byzantine',
        'cackle,    calamities,    calamitous,    calamitously,    calamity,    callous,    calumniate,    calumniation,    calumnies,    calumnious,    calumniously,    calumny,    cancer,    cancerous,    cannibal,    cannibalize,    capitulate,    capricious,    capriciously,    capriciousness,    capsize,    careless,    carelessness,    caricature,    carnage,    carp,    cartoonish,    cash-strapped,    castigate,    castrated,    casualty,    cataclysm,    cataclysmal,    cataclysmic,    cataclysmically,    catastrophe,    catastrophes,    catastrophic,    catastrophically,        caustic,    caustically,    cautionary,    cave,    censure,    chafe,    chaff,    chagrin,    challenging,    chaos,    chaotic,    chasten,    chastise,    chastisement,    chatter,    chatterbox,    cheap,    cheapen,    cheaply,    cheat,    cheated,    cheater,    cheating,    cheats,    checkered,    cheerless,    cheesy,    chide,    childish,    chill,    chilly,    chintzy,    choke,    choleric,    choppy,    chore,    chronic,    chunky,    clamor,    clamorous,    clash,    clique,    clog,    clogged,    clogs,    cloud,    clouding,    cloudy,    clueless,    clumsy,    clunky,    coarse,    cocky,    coerce,    coercion,    coercive,    cold,    coldly,    collapse,    collude,    collusion,    combative,    combust,    comical,    commiserate,    commonplace,    commotion,    commotions,    complacent,    complain,    complained,    complaining,    complains,    complaint,    complaints,    complex,    complicated,    complication,    complicit,    compulsion,    compulsive,    concede,    conceded,    conceit,    conceited,        concern,    concerned,    concerns,    concession,    concessions,    condemn,    condemnable,    condemnation,    condemned,    condemns,    condescend,    condescending,    condescendingly,    condescension,    confess,    confession,    confessions,    confined,    conflict,    conflicted,    conflicting,    conflicts,    confound,    confounded,    confounding,    confront,    confrontation,    confrontational,    confuse,    confused,    confuses,    confusing,    confusion,    confusions,    congested,    congestion,    cons,    conservative,    conspicuous,    conspicuously,    conspiracies,    conspiracy,    conspirator,    conspiratorial,    conspire,    consternation,    contagious,    contaminate,    contaminated,    contaminates,    contaminating,    contamination,    contempt,    contemptible,    contemptuous,    contemptuously,    contend,    contention,    contentious,    contort,    contortions,    contradict,    contradiction,    contradictory,    contrariness,    contravene,    contrive,    contrived,    controversial,    controversy,    convoluted,    corrode,    corrosion,    corrosions,    corrosive,    corrupt,    corrupted,    corrupting,    corruption,    corrupts,    costlier,    costly,    counter-productive,    counterproductive,    covetous,    coward,    cowardly,    crabby,    crack,    cracked,    cracks,    craftily,       crafty,    cramp,    cramped,    cramping,    cranky,    crap,    crappy,    craps,    crash,    crashed,    crashes,    crashing,    crass,    craven,    cravenly,    craze,    crazily,    craziness,    crazy,    creak,    creaking,    creaks,    credulous,    creep,    creeping,    creeps,    creepy,    crept,    crime,    criminal,    cringe,    cringed,    cringes,    cripple,    crippled,    cripples,    crippling,    crisis,    critic,    critical,    criticism,    criticisms,    criticize,    criticized,    criticizing,    critics,    cronyism,    crook,    crooked,    crooks,    crowded,    crowdedness,    crude,    cruel,    crueler,    cruelest,    cruelly,    cruelness,    cruelties,    cruelty,    crumble,    crumbling,    crummy,    crumple,    crumpled,    crumples,    crush,    crushed,    crushing,    cry,    culpable,    culprit,    cumbersome,    curse,    cursed,    curses,    curt,    cuss,    cussed,    cutthroat,    cynical,    cynicism',
        'damage,    damaged,    damages,    damaging,    damn,    damnable,    damnably,    damnation,    damned,    damning,    damper,    danger,    dangerous,    dangerousness,    dark,    darken,    darkened,    darker,    darkness,    dastard,    dastardly,    daunt,    daunting,    dauntingly,    dawdle,    daze,    dazed,    dead,    deadbeat,    deadlock,    deadly,    deadweight,    deaf,    dearth,    death,    debacle,    debase,    debasement,    debaser,    debatable,    debauch,    debaucher,    debauchery,    debilitate,    debilitating,    debility,    debt,    debts,    decadence,    decadent,    decay,    decayed,    deceit,    deceitful,    deceitfully,    deceitfulness,    deceive,    deceiver,    deceivers,    deceiving,    deception,    deceptive,    deceptively,    declaim,    decline,    declines,    declining,    decrement,    decrepit,    decrepitude,    decry,    defamation,    defamations,    defamatory,    defame,    defect,    defective,    defects,    defensive,    defiance,    defiant,    defiantly,    deficiencies,    deficiency,    deficient,    defile,    defiler,    deform,    deformed,    defrauding,    defunct,    defy,    degenerate,    degenerately,    degeneration,    degradation,    degrade,    degrading,    degradingly,    dehumanization,    dehumanize,    deign,    deject,    dejected,    dejectedly,    dejection,    delay,    delayed,    delaying,    delays,    delinquency,    delinquent,    delirious,    delirium,    delude,    deluded,    deluge,    delusion,    delusional,    delusions,    demean,    demeaning,    demise,    demolish,    demolisher,    demon,    demonic,    demonize,    demonized,    demonizes,    demonizing,    demoralize,    demoralizing,    demoralizingly,    denial,    denied,    denies,    denigrate,    denounce,    dense,    dent,    dented,    dents,    denunciate,    denunciation,    denunciations,    deny,    denying,    deplete,    deplorable,    deplorably,    deplore,    deploring,    deploringly,    deprave,    depraved,    depravedly,    deprecate,    depress,    depressed,    depressing,    depressingly,    depression,    depressions,    deprive,    deprived,    deride,    derision,    derisive,    derisively,    derisiveness,    derogatory,    desecrate,    desert,    desertion,    desiccate,    desiccated,    desolate,    desolately,    desolation,    despair,    despairing,    despairingly,    desperate,    desperately,    desperation,    despicable,    despicably,    despise,    despised,    despoil,    despoiler,    despondence,    despondency,    despondent,    despondently,    despot,    despotic,    despotism,    destitute,    destitution,    destroy,    destroyer,    destruction,    destructive,    desultory,    deter,    deteriorate,    deteriorating,    deterioration,    deterrent,    detest,    detestable,    detestably,    detested,    detesting,    detests,    detract,    detracted,    detracting,    detraction,    detracts,    detriment,    detrimental,    devastate,    devastated,    devastates,    devastating,    devastatingly,    devastation,    deviate,    deviation,    devil,    devilish,    devilishly,    devilment,    devilry,    devious,    deviously,    deviousness,    devoid,    diabolic,    diabolical,    diabolically,    diametrically,    diatribe,    diatribes,    dick,    dictator,    dictatorial,    die,    die-hard,    died,    dies,    difficult,    difficulties,    difficulty,    diffidence,    dilapidated,    dilemma,    dilly-dally,    dim,    dimmer,    ding,    dings,    dinky,    dire,    direly,    direness,    dirt,    dirty,    disable,    disabled,    disaccord,    disadvantage,    disadvantaged,    disadvantageous,    disadvantages,    disaffect,    disaffected,    disaffirm,    disagree,    disagreeable,    disagreeably,    disagreed,    disagreeing,    disagreement,    disagrees,    disallow,    disappoint,    disappointed,    disappointing,    disappointingly,    disappointment,    disappointments,    disappoints,    disapprobation,    disapproval,    disapprove,    disapproving,    disarm,    disarray,    disaster,    disastrous,    disastrously,    disavow,    disavowal,    disbelief,    disbelieve,    disbeliever,    disclaim,    discombobulate,    discomfit,       discomfort,    discompose,    disconcert,    disconcerted,    disconcerting,    disconcertingly,    disconsolate,    disconsolately,    disconsolation,    discontent,    discontented,    discontentedly,    discontinued,    discontinuity,    discontinuous,    discord,    discordance,    discordant,    discountenance,    discourage,    discouragement,    discouraging,    discouragingly,    discourteous,    discourteously,    discredit,    discrepant,    discriminate,    discrimination,    discriminatory,    disdain,    disdained,    disdainful,    disdainfully,    disfavor,    disgrace,    disgraced,    disgraceful,    disgracefully,    disgruntle,    disgruntled,    disgust,    disgusted,    disgustedly,    disgustful,    disgustfully,    disgusting,    disgustingly,    dishearten,    disheartening,    dishearteningly,    dishonest,    dishonestly,    dishonesty,    dishonor,    dishonorable,    disillusion,    disillusioned,    disillusionment,    disillusions,    disinclination,    disinclined,    disingenuous,    disingenuously,    disintegrate,    disintegrated,    disintegrates,    disintegration,    disinterest,    disinterested,    dislike,    disliked,    dislikes,    disliking,    dislocated,    disloyal,    disloyalty,    dismal,    dismally,    dismalness,    dismay,    dismayed,    dismaying,    dismayingly,    dismissive,    dismissively,    disobedience,    disobedient,    disobey,    disorder,    disordered,    disorderly,    disorganized,    disorient,    disoriented,    disown,    disparage,    disparaging,    disparagingly,    dispensable,    dispirit,    dispirited,    dispiritedly,    dispiriting,    displace,    displaced,    displease,    displeased,    displeasing,    displeasure,    disproportionate,    disprove,    disputable,    dispute,    disputed,    disquiet,    disquieting,    disquietingly,    disquietude,    disregard,    disregardful,    disreputable,    disrepute,    disrespect,    disrespectable,    disrespectful,    disrespectfully,    disrespectfulness,    disrespecting,    disrupt,    disruption,    disruptive,    dissatisfaction,    dissatisfactory,    dissatisfied,    dissatisfies,    dissatisfy,    dissatisfying,    dissed,    dissemble,    dissembler,    dissension,    dissent,    dissenter,    dissention,    disservice,    disses,    dissidence,    dissident,    dissidents,    dissing,    dissocial,    dissolute,    dissolution,    dissonance,    dissonant,    dissonantly,    dissuade,    dissuasive,    distains,    distaste,    distasteful,    distastefully,    distort,    distorted,    distortion,    distorts,    distract,    distracting,    distraction,    distraught,    distraughtly,    distress,    distressed,    distressing,    distressingly,    distrust,    distrustful,    distrusting,    disturb,    disturbance,    disturbed,    disturbing,    disturbingly,    disunity,    disvalue,    divergent,    divisive,    divisively,    divisiveness,    dizzy,    doddering,    dogged,    doggedly,    dogmatic,    doldrums,    domineer,    domineering,    doom,    doomed,    doomsday,    dope,    doubt,    doubtful,    doubtfully,    doubts,    douchebag,    douchebags,    downbeat,    downcast,    downer,    downfall,    downfallen,    downgrade,    downhearted,    downheartedly,    downhill,    downside,    downsides,    downturn,    downturns,    drab,    draconian,    draconic,    drag,    dragged,    dragging,    dragoon,    drags,    drain,    drained,    draining,    drains,    drastic,    drastically,    drawback,    drawbacks,    dread,    dreadful,    dreadfully,    dreadfulness,    dreary,    dripped,    dripping,    drippy,    drips,    drones,    droop,    droops,    drop-out,    drop-outs,    dropout,    dropouts,    drought,    drowning,    drunk,    drunkard,    drunken,    dubious,    dubiously,    dubitable,    dud,    dull,    dullard,    dumb,    dumbfound,    dump,    dumped,    dumping,    dumps,    dunce,    dungeon,    dungeons,    dupe,    dust,    dusty,    dwindling,    dying',
        'earsplitting,    eccentric,    eccentricity,    effigy,    effrontery,    egocentric,    egomania,    egotism,    egotistical,    egotistically,    egregious,    egregiously,    election-rigger,    elimination,    emaciated,    emasculate,    embarrass,    embarrassing,    embarrassingly,    embarrassment,    embattled,    embroil,    embroiled,    embroilment,    emergency,    emphatic,    emphatically,    emptiness,    encroach,    encroachment,    endanger,    enemies,    enemy,    enervate,    enfeeble,    enflame,    engulf,    enjoin,    enmity,    enrage,    enraged,    enraging,    enslave,    entangle,    entanglement,    entrap,    entrapment,    envious,    enviously,    enviousness,    epidemic,    equivocal,    erase,    erode,    erodes,    erosion,    err,    errant,    erratic,    erratically,    erroneous,    erroneously,    error,    errors,    eruptions,    escapade,    eschew,    estranged,    evade,    evasion,    evasive,    evil,    evildoer,    evils,    eviscerate,    exacerbate,    exaggerate,    exaggeration,    exasperate,    exasperated,    exasperating,    exasperatingly,    exasperation,    excessive,    excessively,    exclusion,    excoriate,    excruciating,    excruciatingly,    excuse,    excuses,    execrate,    exhaust,    exhausted,    exhaustion,    exhausts,       exhort,    exile,    exorbitant,    exorbitantly,    expel,    expensive,    expire,    expired,    explode,    exploit,    exploitation,    explosive,    expropriate,    expropriation,    expulse,    expunge,    exterminate,    extermination,    extinguish,    extort,    extortion,    extraneous,    extravagance,    extravagant,    extravagantly,    extremism,    extremist,    extremists,    eyesore',
        'fuck,    fabricate,    fabrication,    facetious,    facetiously,    fail,    failed,    failing,    fails,    failure,    failures,    faint,    fainthearted,    faithless,    fake,    fall,    fallacies,    fallacious,    fallaciously,    fallaciousness,    fallacy,    fallen,    falling,    fallout,    falls,    FALSE,    falsehood,    falsely,    falsify,    falter,    faltered,    famine,    famished,    fanatic,    fanatical,    fanatically,    fanaticism,    fanatics,    fanciful,    far-fetched,    farce,    farcical,    farcical-yet-provocative,    farcically,    farfetched,    fascism,    fascist,    fastidious,    fastidiously,    fat,    fat-cat,    fat-cats,    fatal,    fatalistic,    fatalistically,    fatally,    fateful,    fatefully,    fathomless,    fatigue,    fatigued,    fatty,    fatuity,    fatuous,    fatuously,    fault,    faults,    faulty,    fawningly,    faze,    fear,    fearful,    fearfully,    fears,    fearsome,    feckless,    feeble,    feebleminded,    feign,    feint,    fell,    felon,    felonious,    ferociously,    ferocity,    fetid,    fever,    feverish,    fevers,    fiasco,    fib,    fibber,    fickle,    fiction,    fictional,    fictitious,    fidget,    fidgety,    fiend,    fiendish,    fierce,    figurehead,    filth,    filthy,    finagle,    finicky,    fissures,    fist,    flabbergast,    flabbergasted,    flagging,    flagrant,    flagrantly,    flair,    flairs,    flak,    flake,    flakey,    flaking,    flaky,    flare,    flares,    flat-out,    flaunt,    flaw,    flawed,    flaws,    flee,    fleeing,    fleer,    flees,    fleeting,    flicker,    flickering,    flickers,    flighty,    flimflam,    flimsy,    flirt,    flirty,    floored,    flounder,    floundering,    flout,    fluster,    foe,    fool,    fooled,    foolhardy,    foolish,    foolishly,    foolishness,    forbid,    forbidden,    forbidding,    forceful,    foreboding,    forebodingly,    forfeit,    forged,    forgetful,    forgetfully,    forgetfulness,    forlorn,    forlornly,    forsake,    forsaken,    forswear,    foul,    foully,    foulness,    fractious,    fractiously,    fracture,    fragile,    fragmented,    frail,    frantic,    frantically,    franticly,    fraud,    fraudulent,    fraught,    frazzle,    frazzled,    freak,    freaking,    freakish,    freakishly,    freaks,    freeze,    freezes,    freezing,    frenetic,    frenetically,    frenzied,    frenzy,    fret,    fretful,    frets,    friction,    frictions,    fried,    frigging,    fright,    frighten,    frightening,    frighteningly,    frightful,    frightfully,    frigid,    frost,    frown,    froze,    frozen,    fruitless,    fruitlessly,    frustrate,    frustrated,    frustrates,    frustrating,    frustratingly,    frustration,    frustrations,    f”ck,    f”cking,    fudge,    fugitive,    full-blown,    fulminate,    fumble,    fume,    fumes,    fundamentalism,    funky,    funnily,    funny,    furious,    furiously,    furor,    fury,    fuss,    fussy,    fustigate,    fusty,    futile,    futilely,    futility,    fuzzy',
        'gabble,    gaff,    gaffe,    gainsay,    gainsayer,    gall,    galling,    gallingly,    galls,    gangster,    gape,    garbage,    garish,    gasp,    gauche,    gaudy,    gawk,    gawky,    geezer,    genocide,    get-rich,    ghastly,    ghetto,    ghosting,    gibber,    gibberish,    gibe,    giddy,    gimmick,    gimmicked,    gimmicking,    gimmicks,    gimmicky,    glare,    glaringly,    glib,    glibly,    glitch,    glitches,    gloatingly,    gloom,    gloomy,    glower,    glum,    glut,    gnawing,    goad,    goading,    god-awful,    goof,    goofy,    goon,    gossip,    graceless,    gracelessly,    graft,    grainy,    grapple,    grate,    grating,    gravely,    greasy,    greed,    greedy,    grief,    grievance,    grievances,    grieve,    grieving,    grievous,    grievously,    grim,    grimace,    grind,    gripe,    gripes,    grisly,    gritty,    gross,    grossly,    grotesque,    grouch,    grouchy,    groundless,    grouse,    growl,    grudge,    grudges,    grudging,    grudgingly,    gruesome,    gruesomely,    gruff,    grumble,    grumpier,    grumpiest,    grumpily,    grumpy,    guile,    guilt,    guiltily,    guilty,    gullible,    gutless,    gutter',
        'hack,    hacks,    haggard,    haggle,    halfhearted,    halfheartedly,    hallucinate,    hallucination,    hamper,    hampered,    handicapped,    hang,    hangs,    haphazard,    hapless,    harangue,    harass,    harassed,    harasses,    harassment,    harboring,    harbors,    hard,    hard-hit,    hard-liner,    hardball,    harden,    hardened,    hardheaded,    hardhearted,    hardliner,    hardliners,    hardship,    hardships,    harm,    harmed,    harmful,    harms,    harpy,    harridan,    harried,    harrow,    harsh,    harshly,    hassle,    hassled,    hassles,    haste,    hastily,    hasty,    hate,    hated,    hateful,    hatefully,    hatefulness,    hater,    haters,    hates,    hating,    hatred,    haughtily,    haughty,    haunt,    haunting,    havoc,    hawkish,    haywire,    hazard,    hazardous,    haze,    hazy,    head-aches,    headache,    headaches,    heartbreaker,    heartbreaking,    heartbreakingly,    heartless,    heathen,    heavy-handed,    heavyhearted,    heck,    heckle,    heckled,    heckles,    hectic,    hedge,    hedonistic,    heedless,    hefty,    hegemony,    heinous,    hell,    hell-bent,    hellion,    hells,    helpless,    helplessly,    helplessness,    heresy,    heretic,    heretical,    hesitant,    hideous,    hideously,    hideousness,    high-priced,    hinder,    hindrance,    hiss,    hissed,    hissing,    ho-hum,    hoard,    hoax,    hobble,    hogs,    hollow,    hoodwink,    hooligan,    hopeless,    hopelessly,    hopelessness,    horde,    horrendous,    horrendously,    horrible,    horrid,    horrific,    horrified,    horrifies,    horrify,    horrifying,    hostage,    hostile,    hostilities,    hostility,    hotbeds,    hothead,    hotheaded,    hothouse,    hubris,    huckster,    hum,    humid,    humiliate,    humiliating,    humiliation,    humming,    hung,    hurt,    hurtful,    hurting,    hurts,    hustler,    hype,    hypocrisy,    hypocrite,    hypocrites,    hypocritical,    hypocritically,    hysteria,    hysteric,    hysterical,    hysterically,    hysterics',
        'idiocies,    idiocy,    idiot,    idiotic,    idiotically,    idiots,    idle,    ignoble,    ignominious,    ignominiously,    ignominy,    ignorance,    ignorant,    ignore,    ill-advised,    ill-conceived,    ill-defined,    ill-designed,    ill-fated,    ill-favored,    ill-formed,    ill-mannered,    ill-natured,    ill-sorted,    ill-tempered,    ill-treated,    ill-treatment,    ill-usage,    ill-used,    illegal,    illegally,    illegitimate,    illicit,    illiterate,    illness,    illogical,    illogically,    illusion,    illusions,    illusory,    imaginary,    imbalance,    imbecile,    imbroglio,    immaterial,    immature,    imminence,    imminently,    immobilized,    immoderate,    immoderately,    immodest,    immoral,    immorality,    immorally,    immovable,    impair,    impaired,    impasse,    impatience,    impatient,    impatiently,    impeach,    impedance,    impede,    impediment,    impending,    impenitent,    imperfect,    imperfection,    imperfections,    imperfectly,    imperialist,    imperil,    imperious,    imperiously,    impermissible,    impersonal,    impertinent,    impetuous,    impetuously,    impiety,    impinge,    impious,    implacable,    implausible,    implausibly,    implicate,    implication,    implode,    impolite,    impolitely,    impolitic,    importunate,    importune,    impose,    imposers,    imposing,    imposition,    impossible,       impossibly,    impotent,    impoverish,    impoverished,    impractical,    imprecate,    imprecise,    imprecisely,    imprecision,    imprison,    imprisonment,    improbability,    improbable,    improbably,    improper,    improperly,    impropriety,    imprudence,    imprudent,    impudence,    impudent,    impudently,    impugn,    impulsive,    impulsively,    impunity,    impure,    impurity,    inability,    inaccuracies,    inaccuracy,    inaccurate,    inaccurately,    inaction,    inactive,    inadequacy,    inadequate,    inadequately,    inadvisable,    inane,    inanely,    inappropriate,    inappropriately,    inapt,    inarticulate,    inattentive,    inaudible,    incapable,    incapably,    incautious,    incendiary,    incense,    incessant,    incessantly,    incite,    incitement,    incivility,    inclement,    incoherence,    incoherent,    incoherently,    incommensurate,    incomparable,    incomparably,    incompatibility,    incompatible,    incompetence,    incompetent,    incompetently,    incomplete,    incomprehensible,    incomprehension,    inconceivable,    inconceivably,    incongruous,    incongruously,    inconsequential,    inconsequentially,    inconsiderate,    inconsiderately,    inconsistencies,    inconsistency,    inconsistent,    inconsolable,    inconsolably,    inconstant,    inconvenience,    inconveniently,    incorrect,    incorrectly,    incorrigible,    incorrigibly,    incredulous,    incredulously,    inculcate,    indecency,    indecent,    indecently,    indecision,    indecisive,    indecisively,        indefensible,    indelicate,    indeterminable,    indeterminably,    indeterminate,    indifference,    indifferent,    indigent,    indignant,    indignantly,    indignation,    indignity,    indiscernible,    indiscreet,    indiscreetly,    indiscretion,    indiscriminate,    indiscriminately,      indistinguishable,    indoctrinate,    indoctrination,    indolent,    indulge,    ineffective,    ineffectively,    ineffectiveness,    ineffectual,    ineffectually,        inefficacy,    inefficiency,    inefficient,    inefficiently,    inelegance,    inelegant,    ineligible,       inept,    ineptitude,    ineptly,    inequalities,    inequality,    inequitable,    inequitably,    inequities,    inescapable,    inescapably,    inessential,    inevitable,    inevitably,    inexcusable,    inexcusably,    inexorable,    inexorably,    inexperience,    inexperienced,    inexpert,    inexpertly,    inexpiable,    inextricable,    inextricably,    infamous,    infamously,    infamy,    infected,    infection,    infections,    inferior,    inferiority,    infernal,    infest,    infested,    infidel,    infidels,    infiltrator,    infiltrators,    infirm,    inflame,    inflammation,    inflammatory,        inflated,    inflationary,    inflexible,    inflict,    infraction,    infringe,    infringement,    infringements,    infuriate,    infuriated,    infuriating,    infuriatingly,    inglorious,    ingrate,    ingratitude,    inhibit,    inhibition,    inhospitable,       inhuman,    inhumane,    inhumanity,    inimical,    inimically,    iniquitous,    iniquity,    injudicious,    injure,   injurious,    injury,    injustice,    injustices,    innuendo,    inoperable,    inopportune,    inordinate,    inordinately,    insane,    insanely,    insanity,    insatiable,    insecure,    insecurity,    insensible,    insensitive,    insensitively,    insensitivity,    insidious,    insidiously,    insignificance,    insignificant,    insignificantly,    insincere,    insincerely,    insincerity,    insinuate,    insinuating,    insinuation,    insolence,    insolent,    insolently,    insolvent,    insouciance,    instability,    instigate,    instigator,    instigators,    insubordinate,    insubstantial,    insubstantially,    insufferable,    insufferably,    insufficiency,    insufficient,    insufficiently,    insular,    insult,    insulted,    insulting,    insultingly,    insults,    insupportable,        insurmountable,    insurmountably,    insurrection,    intense,    interfere,    interference,    interferes,    intermittent,    interrupt,    interruption,    interruptions,    intimidate,    intimidating,    intimidatingly,    intimidation,    intolerable,    intolerance,    intoxicate,    intractable,    intransigence,    intransigent,    intrude,    intrusion,    intrusive,    inundate,    inundated,    invader,    invalid,    invalidate,    invalidity,    invasive,    invective,    inveigle,    invidious,    invidiously,    invidiousness,    invisible,    involuntarily,    involuntary,    irascible,    irate,    irately,    ire,    irk,    irked,    irking,    irks,    irksome,    irksomely,    irksomeness,    ironic,    ironical,    ironically,    ironies,    irony,    irrational,        irrationality,    irrationally,    irrationals,    irreconcilable,    irrecoverable,        irrecoverably,    irredeemable,    irredeemably,    irregular,    irregularity,    irrelevance,    irrelevant,    irreparable,    irrepressible,    irresolute,       irresponsible,    irresponsibly,       irretrievable,    irreversible,    irritable,    irritably,    irritant,    irritate,    irritated,    irritating,    irritation,    irritations,    isolate,    isolated,    isolation,    issue,    issues,    itch,    itching,    itchy',
        'jabber,    jaded,    jagged,    jam,    jarring,    jaundiced,    jealous,    jealously,    jealousness,    jealousy,    jeer,    jeering,    jeeringly,    jeers,    jeopardize,    jeopardy,    jerk,    jerky,    jitter,    jitters,    jittery,    job-killing,    jobless,    joke,    joker,    jolt,    judder,    juddering,    judders,    jumpy,    junk,    junky,    junkyard',
        'kill,    killed,    killer,    killing,    killjoy,    kills,    knave,    knife,    knock,    knotted,    kook,    kooky',
        'lack,    lackadaisical,    lacked,    lackey,    lackeys,    lacking,    lackluster,    lacks,    laconic,    lag,    lagged,    lagging,    lags,    laid-off,    lambast,    lambaste,    lame,    lame-duck,    lament,    lamentable,    lamentably,    languid,    languish,    languor,    languorous,    languorously,    lanky,    lapse,    lapsed,    lapses,    lascivious,    last-ditch,    latency,    laughable,    laughably,    laughingstock,    lawbreaker,    lawbreaking,    lawless,    lawlessness,    layoff,    layoff-happy,    lazy,    leak,    leakage,    leakages,    leaking,    leaks,    leaky,    lecher,    lecherous,    lechery,    leech,    leer,    leery,    left-leaning,    lemon,    lengthy,    less-developed,    lesser-known,    letch,    lethal,    lethargic,    lethargy,    lewd,    lewdly,    lewdness,    liability,    liable,    liar,    liars,    licentious,    licentiously,    licentiousness,    lie,    lied,    lies,    life-threatening,    lifeless,    limit,    limitation,    limitations,    limited,    limits,    limp,    listless,    litigious,    little-known,    livid,    lividly,    loath,    loathe,    loathing,    loathly,    loathsome,    loathsomely,    lone,    loneliness,    lonely,    loner,    lonesome,    long-time,    long-winded,    longing,    longingly,    loophole,    loopholes,    loose,    loot,   lose,    loser,    losers,    loses,    losing,    loss,    losses,    lost,    loud,    louder,    lousy,    loveless,    lovelorn,    low-rated,    lowly,    ludicrous,    ludicrously,    lugubrious,    lukewarm,    lull,    lumpy,    lunatic,     lurch,    lure,    lurid,    lurk,    lurking,    lying',
        'macabre,    mad,    madden,    maddening,    maddeningly,    madder,    madly,    madman,    madness,    maladjusted,    maladjustment,    malady,    malaise,    malcontent,    malcontented,    maledict,    malevolence,    malevolent,    malevolently,    malice,    malicious,    maliciously,    maliciousness,    malign,    malignant,    malodorous,    maltreatment,    mangle,    mangled,    mangles,    mangling,    mania,    maniac,    maniacal,    manic,    manipulate,    manipulation,    manipulative,    manipulators,    mar,    marginal,    marginally,    martyrdom,    martyrdom-seeking,    mashed,    massacre,    massacres,    matte,    mawkish,    mawkishly,    mawkishness,    meager,    meaningless,    meanness,    measly,    meddle,    meddlesome,    mediocre,    mediocrity,    melancholy,    melodramatic,    melodramatically,    meltdown,    menace,    menacing,    menacingly,    mendacious,    mendacity,    menial,    merciless,    mercilessly,    mess,    messed,    messes,    messing,    messy,    midget,    miff,    militancy,    mindless,    mindlessly,    mirage,    mire,    misalign,    misaligned,    misaligns,    misapprehend,    misbecome,    misbecoming,    misbegotten,    misbehave,    misbehavior,    miscalculate,    miscalculation,    miscellaneous,    mischief,    mischievous,    mischievously,    misconception,    misconceptions,    miscreant,    miscreants,    misdirection,    miser,    miserable,    miserableness,    miserably,    miseries,    miserly,    misery,    misfit,    misfortune,    misgiving,    misgivings,    misguidance,    misguide,    misguided,    mishandle,    mishap,    misinform,    misinformed,    misinterpret,    misjudge,    misjudgment,    mislead,    misleading,    misleadingly,      mismanage,    mispronounce,    mispronounced,    mispronounces,    misread,    misreading,    misrepresent,    misrepresentation,    miss,    missed,    misses,    misstatement,    mist,    mistake,    mistaken,    mistakenly,    mistakes,    mistress,    mistrust,    mistrustful,    mistrustfully,    mists,    misunderstand,    misunderstanding,    misunderstandings,    misunderstood,    misuse,    moan,    mobster,    mock,    mocked,    mockeries,    mockery,    mocking,    mockingly,    mocks,    molest,    molestation,    monotonous,    monotony,    monster,    monstrosities,    monstrosity,    monstrous,    monstrously,    moody,    moot,    mope,    morbid,    morbidly,    mordant,    mordantly,    moribund,    moron,    moronic,    morons,    mortification,    mortified,    mortify,    mortifying,    motionless,    motley,    mourn,    mourner,    mournful,    mournfully,    muddle,    muddy,    mudslinger,    mudslinging,    mulish,    multi-polarization,    mundane,    murder,    murderer,    murderous,    murderously,    murky,    muscle-flexing,    mushy,    musty,    mysterious,    mysteriously,    mystery,    mystify,    myth',
        'nag,    nagging,    naive,    naively,    narrower,    nastily,    nastiness,    nasty,    naughty,    nauseate,    nauseates,    nauseating,    nauseatingly,    naïve,    nebulous,    nebulously,    needless,    needlessly,    needy,    nefarious,    nefariously,    negate,    negation,    negative,    negatives,    negativity,    neglect,    neglected,    negligence,    negligent,    nemesis,    nepotism,    nervous,    nervously,    nervousness,    nettle,    nettlesome,    neurotic,    neurotically,    niggle,    niggles,    nightmare,    nightmarish,    nightmarishly,    nitpick,    nitpicking,    noise,    noises,    noisier,    noisy,    non-confidence,    nonexistent,    nonresponsive,    nonsense,    nosey,    notoriety,    notorious,    notoriously,    noxious,    nuisance,    numb',
        'obese,    object,    objection,    objectionable,    objections,    oblique,    obliterate,    obliterated,    oblivious,    obnoxious,    obnoxiously,    obscene,    obscenely,    obscenity,    obscure,    obscured,    obscures,    obscurity,    obsess,    obsessive,    obsessively,    obsessiveness,    obsolete,    obstacle,    obstinate,    obstinately,    obstruct,    obstructed,    obstructing,    obstruction,    obstructs,    obtrusive,    obtuse,    occlude,    occluded,    occludes,    occluding,    odd,    odder,    oddest,    oddities,    oddity,    oddly,    odor,    offence,    offend,    offender,    offending,    offenses,    offensive,    offensively,    offensiveness,    officious,    ominous,    ominously,    omission,    omit,    one-sided,    onerous,    onerously,    onslaught,    opinionated,    opponent,    opportunistic,    oppose,    opposition,    oppositions,    oppress,    oppression,    oppressive,    oppressively,    oppressiveness,    oppressors,    ordeal,    orphan,    ostracize,    outbreak,    outburst,    outbursts,    outcast,    outcry,    outlaw,    outmoded,    outrage,    outraged,    outrageous,    outrageously,    outrageousness,    outrages,    outsider,    over-acted,    over-awe,    over-balanced,    over-hyped,    over-priced,    over-valuation,    overact,    overacted,    overawe,    overbalance,    overbalanced,    overbearing,    overbearingly,    overblown,    overdo,    overdone,    overdue,    overemphasize,    overheat,    overkill,    overloaded,    overlook,    overpaid,    overplay,    overpower,    overpriced,    overrated,    overreach,    overrun,    overshadow,    oversight,    oversights,    oversimplification,    oversimplified,    oversimplify,    oversize,    overstate,    overstated,    overstatement,    overstatements,    overstates,    overtaxed,    overthrow,    overthrows,    overturn,    overweight,    overwhelm,    overwhelmed,    overwhelming,    overwhelmingly,    overwhelms,    overzealous,    overzealously',
        'pain,    painful,    painfully,    pains,    pale,    pales,    paltry,    pan,    pandemonium,    pander,    pandering,    panders,    panic,    panicked,    panicking,    panicky,    paradoxical,    paradoxically,        paralyzed,    paranoia,    paranoid,    parasite,    pariah,    parody,    partiality,    partisan,    partisans,        passive,    passiveness,    pathetic,    pathetically,    patronize,    paucity,    pauper,    paupers,    payback,    peculiar,    peculiarly,    pedantic,    peeled,    peeve,    peeved,    peevish,    peevishly,    penalize,    penalty,    perfidious,    perfunctory,    peril,    perilous,    perilously,    perish,    pernicious,    perplex,    perplexed,    perplexing,    perplexity,    persecute,    persecution,    pertinacious,    pertinaciously,    pertinacity,    perturb,    perturbed,    pervasive,    perverse,    perversely,    perversion,    perversity,    pervert,    perverted,    perverts,    pessimism,    pessimistic,    pessimistically,    pest,    pestilent,    petrified,    petrify,    pettifog,    petty,    phobia,    phobic,    phony,    picket,    picketed,    picketing,    pickets,    picky,    pig,    pigs,    pillage,    pillory,    pimple,    pinch,    pique,    pitiable,    pitiful,    pitifully,    pitiless,    pitilessly,    pittance,    pity,    plagiarize,    plague,    plaything,    plea,    pleas,    plebeian,    plight,    plot,    plotters,    ploy,    plunder,    plunderer,    pointless,    pointlessly,    poison,    poisonous,    poisonously,    pokey,    poky,    pollute,    polluter,    polluters,    pompous,    poor,    poorer,    poorest,    poorly,    posturing,    pout,    poverty,    powerless,    prate,    pratfall,    prattle,    precarious,    precariously,    precipitate,    precipitous,    predatory,    predicament,    prejudge,    prejudice,    prejudices,    prejudicial,    premeditated,    preoccupy,    preposterous,    preposterously,    presumptuous,    presumptuously,        pretend,    pretense,    pretentious,    pretentiously,    prevaricate,    pricey,    pricier,    prick,    prickle,    prickles,    prideful,   primitive,    prison,    prisoner,    problem,    problematic,    problems,    procrastinate,    procrastinates,    procrastination,    profane,    profanity,    prohibit,    prohibitive,    prohibitively,    propaganda,    propagandize,    proprietary,    prosecute,    protest,    protested,    protesting,    protests,    protracted,    provocation,    provocative,    provoke,    pry,    pugnacious,    pugnaciously,    pugnacity,    punch,    punish,    punishable,    punitive,    punk,    puny,    puppet,    puppets,    puzzled,    puzzlement,    puzzling',
        'quack,    qualm,    qualms,    quandary,    quarrel,     quarrels,    quarrelsome,    quash,    queer,    questionable,    quibble,    quibbles,    quitter',
        'rabid,    racism,    racist,    racists,    racy,    radical,    radicalization,    radically,    radicals,    rage,    ragged,    raging,    rail,    raked,    rampage,    rampant,    ramshackle,    rancor,    randomly,    rankle,    rant,    ranted,    ranting,    rants,    rape,    raped,    raping,    rascal,    rascals,    rash,    rattle,    rattled,    rattles,    ravage,    raving,    reactionary,    rebellious,    rebuff,    rebuke,    recalcitrant,    recant,    recession,    recessionary,    reckless,    recklessly,    recklessness,    recoil,    recourses,    redundancy,    redundant,    refusal,    refuse,    refused,    refuses,    refusing,    refutation,    refute,    refuted,    refutes,    refuting,    regress,    regression,    regressive,    regret,    regretful,    regretfully,    regrets,    regrettable,    regrettably,    regretted,    reject,    rejected,    rejecting,    rejection,    rejects,    relapse,    relentless,    relentlessly,    relentlessness,    reluctance,    reluctant,    reluctantly,    remorse,    remorseful,    remorsefully,    remorseless,    remorselessly,    remorselessness,    renounce,    renunciation,    repel,    repetitive,    reprehensible,    reprehensibly,    reprehension,    reprehensive,    repress,    repression,    repressive,    reprimand,    reproach,    reproachful,    reprove,    reprovingly,    repudiate,    repudiation,    repugnance,    repugnant,    repugnantly,    repulse,    repulsed,    repulsing,    repulsive,    repulsively,    repulsiveness,    resent,    resentful,    resentment,    resignation,    resigned,    resistance,    restless,    restlessness,    restrict,    restricted,    restriction,    restrictive,    resurgent,    retaliate,    retaliatory,    reticent,    retract,    retreat,    retreated,    revenge,    revengeful,    revengefully,    revert,    revile,    reviled,    revoke,    revolt,    revolting,    revoltingly,    revulsion,    revulsive,    rhapsodize,    rhetoric,    rhetorical,    ricer,    ridicule,    ridicules,    ridiculous,    ridiculously,    rife,    rift,    rifts,    rigid,    rigidity,    rigidness,    rile,    riled,    rip,    rip-off,    ripped,    risk,    risks,    risky,    rival,    rivalry,    roadblocks,    rocky,    rogue,    rollercoaster,    rot,    rotten,    rough,    rubbish,    rude,    rue,    ruffian,    ruffle,    ruin,    ruined,    ruining,    ruinous,    ruins,    rumbling,    rumor,    rumors,    rumple,    run-down,    runaway,    rupture,    rust,    rusts,    rusty,    rut,    ruthless,    ruthlessly,    ruthlessness,    ruts',
        'sabotage,    sack,    sacrificed,    sad,    sadden,    sadly,    sadness,    sag,    sagged,    sagging,    saggy,    sags,    salacious,    sanctimonious,    sap,    sarcasm,    sarcastic,    sarcastically,    sardonic,    sardonically,    sass,    satirical,    satirize,    savage,    savaged,    savagery,    savages,    scaly,    scam,    scams,    scandal,    scandalize,    scandalized,    scandalous,    scandalously,    scandals,    scant,    scapegoat,    scar,    scarce,    scarcely,    scarcity,    scare,    scared,    scarier,    scariest,    scarily,    scarred,    scars,    scary,    scathing,    scathingly,   scoff,    scold,    scolded,    scolding,    scorching,        scorn,    scornful,    scornfully,    scoundrel,    scourge,    scowl,    scramble,    scrambled,    scrambles,    scrambling,    scrap,    scratch,    scratched,    scratches,    scratchy,    scream,    screech,    screw-up,    screwed,    screwed-up,    screwy,    scuff,    scuffs,    scum,    scummy,    second-class,    second-tier,    secretive,    sedentary,    seedy,    seethe,    seething,    self-coup,    self-criticism,    self-defeating,    self-destructive,    self-humiliation,    self-interest,    self-interested,    self-serving,     selfish,    selfishly,    selfishness,    senile,    sensationalize,    senseless,    senselessly,    seriousness,    sermonize,    servitude,    set-up,    setback,    setbacks,    sever,    severe,    severity,        shabby,    shadowy,    shady,    shake,    shaky,    shallow,    sham,    shambles,    shame,    shameful,    shamefully,    shamefulness,    shameless,    shamelessly,    shamelessness,    shark,    sharply,    shatter,    shimmer,    shimmy,    shipwreck,    shirk,    shirker,    shiver,    shock,    shocked,    shocking,    shockingly,    shoddy,    short-lived,    shortage,    shortchange,    shortcoming,    shortcomings,    shortness,    shortsighted,    shortsightedness,    showdown,    shrew,    shriek,    shrill,    shrilly,    shrivel,    shroud,    shrouded,    shrug,    shun,    shunned,    sick,    sicken,    sickening,    sickeningly,    sickly,    sickness,    sidetrack,    sidetracked,    siege,    silly,    simplistic,    simplistically,    sin,    sinful,    sinfully,    sinister,    sinisterly,    sink,    sinking,    skeletons,    skeptic,    skeptical,    skeptically,    skepticism,    sketchy,    skimpy,    skinny,    skittish,    skittishly,    skulk,    slack,    slander,    slanderer,    slanderous,    slanderously,    slanders,    slap,    slashing,    slaughter,    slaughtered,    slave,    slaves,    sleazy,    slime,    slog,    slogged,    slogging,    slogs,    sloppily,    sloppy,    sloth,    slothful,    slow,    slow-moving,    slowed,    slower,    slowest,    slowly,    slug,    sluggish,    slump,    slumping,    slur,    sly,    smack,    smallish,    smash,    smear,    smell,    smelled,    smelling,    smells,    smelly,    smelt,    smoke,    smokescreen,    smolder,    smoldering,    smother,    smudge,    smudged,    smudges,    smudging,    smug,    smugly,    snag,    snagged,    snagging,    snags,    snappish,    snappishly,    snare,    snarky,    snarl,    sneak,    sneakily,    sneaky,    sneer,    sneering,    sneeringly,    snob,    snobbish,    snobby,    snobs,    snub,    soapy,    sob,    sober,    sobering,    solemn,    solicitude,    somber,    sore,    sorely,    soreness,    sorrow,    sorrowful,    sorrowfully,    sorry,    sour,    sourly,    spade,    spank,    spew,    spewed,    spewing,    spews,    spilling,    spinster,    spiritless,    spite,    spiteful,    spitefully,    spitefulness,    splatter,    split,    splitting,    spoil,    spoilage,    spoilages,    spoiled,    spoils,    spook,    spookier,    spookiest,    spookily,    spooky,    spoon-fed,    spoon-feed,    sporadic,    spotty,    spurious,    spurn,    sputter,    squabble,    squabbling,    squander,    squash,    squeak,    squeaks,    squeaky,    squeal,    squealing,    squeals,    squirm,    stab,    stagnant,    stagnate,    stagnation,    staid,    stain,    stains,    stale,    stalemate,    stall,    stalls,    stammer,    stampede,    standstill,    stark,    starkly,    startle,    startling,    startlingly,    starvation,    starve,    static,    steal,    stealing,    steals,    steep,    steeply,    stench,    stereotype,    stereotypical,    stereotypically,    stern,    stew,    sticky,    stiff,    stiffness,    stifle,    stifling,    stiflingly,    stigma,    stigmatize,    sting,    stinging,    stingingly,    stingy,    stink,    stinks,    stodgy,    stole,    stolen,    stooge,    stooges,    stormy,    straggle,    straggler,    strain,    strained,    straining,    strange,    strangely,    stranger,    strangest,    strangle,    streaky,    strenuous,    stress,    stresses,    stressful,    stressfully,    stricken,    strict,    strictly,    strident,    stridently,    strife,    strike,    stringent,    stringently,    struck,    struggle,    struggled,    struggles,    struggling,    strut,    stubborn,    stubbornly,    stubbornness,    stuck,    stuffy,    stumble,    stumbled,    stumbles,    stump,    stumped,    stumps,    stun,    stunt,    stunted,    stupid,    stupidest,    stupidity,    stupidly,    stupor,    stutter,    stuttered,    stuttering,    stutters,    sty,    stymied,    sub-par,    subdued,    subjected,    subjection,    subjugate,    subjugation,    submissive,    subordinate,    subpoena,    subpoenas,    subservience,    subservient,    substandard,    subtract,    subversion,    subversive,    subversively,    subvert,    succumb,    suck,    sucked,    sucker,    sucks,    sucky,    sue,    sued,    sues,    suffer,    suffered,    sufferer,    sufferers,    suffering,    suffers,    suffocate,    sugar-coat,    sugar-coated,    sugarcoated,    suicidal,    suicide,    sulk,    sullen,    sully,    sunder,    sunk,    sunken,    superficial,    superficiality,    superficially,    superfluous,    superstition,    superstitious,    suppress,    suppression,    surrender,    susceptible,    suspect,    suspicion,    suspicions,    suspicious,    suspiciously,    swagger,    swamped,    sweaty,    swelled,    swelling,    swindle,    swipe,    swollen,    symptom,    symptoms,    syndrome',
        'taboo,    tacky,    taint,    tainted,    tamper,    tangle,    tangled,    tangles,    tank,    tanked,    tanks,    tantrum,    tardy,    tarnish,    tarnished,    tarnishes,    tarnishing,    tattered,    taunt,    taunting,    tauntingly,    taunts,    taut,    tawdry,    taxing,    tease,    teasingly,    tedious,    tediously,    temerity,    temper,    tempest,    temptation,    tenderness,    tense,    tension,    tentative,    tentatively,    tenuous,    tenuously,    tepid,    terrible,    terribleness,    terribly,    terror,    terror-genic,    terrorism,    terrorize,    testily,    testy,    tetchily,    tetchy,    thankless,    thicker,    thirst,    thorny,    thoughtless,    thoughtlessly,    thoughtlessness,    thrash,    threat,    threaten,    threatening,    threats,    threesome,    throb,    throbbed,    throbbing,    throbs,    throttle,    thug,    thumb-down,    thumbs-down,    thwart,    time-consuming,    timid,    timidity,    timidly,    tin-y,    tingled,    tingling,    tired,    tiresome,    tiring,    tiringly,    toil,    toll,    top-heavy,    topple,    torment,    tormented,    torrent,    tortuous,    torture,    tortured,    tortures,    torturing,    torturous,    torturously,    totalitarian,    touchy,    toughness,    tout,    touted,    touts,    toxic,    traduce,    tragedy,    tragic,    tragically,    traitor,    traitorous,    traitorously,    tramp,    trample,    transgress,    transgression,    trap,    trapped,    trash,    trashed,    trashy,    trauma,    traumatic,    traumatically,    traumatize,    traumatized,    travesties,    travesty,    treacherous,    treacherously,    treachery,    treason,    treasonous,    trick,    tricked,    trickery,    tricky,    trivial,    trivialize,    trouble,    troubled,    troublemaker,    troubles,    troublesome,    troublesomely,    troubling,    troublingly,    truant,    tumble,    tumbled,    tumbles,    tumultuous,    turbulent,    turmoil,    twist,    twisted,    twists,    two-faced,    two-faces,    tyrannical,    tyrannically,    tyranny,    tyrant',
        'ugh,    uglier,    ugliest,    ugliness,    ugly,    ulterior,    ultimatum,    ultimatums,    ultra-hardline,    un-viewable,    unable,    unacceptable,    unacceptably,        unaccustomed,    unachievable,    unaffordable,    unappealing,    unattractive,    unauthentic,    unavailable,    unavoidably,    unbearable,    unbelievable,    unbelievably,    uncaring,    uncertain,    uncivil,    uncivilized,    unclean,    unclear,    uncollectible,    uncomfortable,    uncomfortably,       uncompetitive,    uncompromising,    uncompromisingly,    unconfirmed,    unconstitutional,    uncontrolled,    unconvincing,    unconvincingly,    uncooperative,    uncouth,    uncreative,    undecided,    undefined,    undependability,    undependable,    undercut,    undercuts,    undercutting,    underdog,    underestimate,    underlings,    undermine,    undermined,    undermines,    undermining,    underpaid,    underpowered,    undersized,    undesirable,    undetermined,    undid,    undignified,    undissolved,    undocumented,    undone,    undue,    unease,    uneasily,    uneasiness,    uneasy,    uneconomical,    unemployed,    unequal,    unethical,    uneven,    uneventful,    unexpected,    unexpectedly,    unexplained,    unfairly,    unfaithful,    unfaithfully,    unfamiliar,    unfavorable,    unfeeling,    unfinished,    unfit,    unforeseen,    unforgiving,    unfortunate,    unfortunately,    unfounded,    unfriendly,    unfulfilled,    unfunded,    ungovernable,    ungrateful,    unhappily,    unhappiness,    unhappy,    unhealthy,    unhelpful,    unilateralism,    unimaginable,    unimaginably,    unimportant,    uninformed,    uninsured,    unintelligible,      unipolar,    unjust,    unjustifiable,    unjustifiably,    unjustified,    unjustly,    unkind,    unkindly,    unknown,       unlawful,    unlawfully,    unlawfulness,    unleash,    unlicensed,    unlikely,    unlucky,    unmoved,    unnatural,    unnaturally,    unnecessary,    unneeded,    unnerve,    unnerved,    unnerving,    unnervingly,    unnoticed,    unobserved,    unorthodox,    unorthodoxy,    unpleasant,    unpopular,    unpredictable,    unprepared,    unproductive,    unprofitable,    unproved,    unproven,    unqualified,    unravel,    unraveled,    unreachable,    unreadable,    unrealistic,    unreasonable,    unreasonably,    unrelenting,    unrelentingly,    unreliability,    unreliable,    unresolved,    unresponsive,    unrest,    unruly,    unsafe,    unsatisfactory,    unsavory,    unscrupulous,    unscrupulously,    unsecure,    unseemly,    unsettle,    unsettled,    unsettling,    unsettlingly,    unskilled,    unsophisticated,    unsound,    unspeakable,    unspecified,    unstable,    unsteadily,    unsteadiness,    unsteady,    unsuccessful,    unsuccessfully,    unsupported,    unsupportive,    unsure,    unsuspecting,    unsustainable,    untenable,    untested,    unthinkable,    unthinkably,    untimely,    untouched,    untrue,    untrustworthy,    untruthful,    unusable,    unusably,    unusual,    unusually,    unwanted,    unwarranted,    unwatchable,    unwelcome,    unwell,    unwieldy,    unwilling,    unwillingly,    unwillingness,    unwise,    unwisely,    unworkable,    unworthy,    unyielding,    upbraid,    upheaval,    uprising,    uproar,    uproarious,    uproariously,    uproot,    upset,    upsets,    upsetting,    upsettingly,    urgent,    useless,    usurp,    usurper,    utterly',
        'vagrant,    vague,    vagueness,    vain,    vainly,    vanity,    vehement,    vehemently,    vengeance,    vengeful,    vengefully,    vengefulness,    venom,    venomous,    venomously,    vent,    vestiges,    vex,    vexation,    vexing,    vexingly,    vibrate,    vibrated,    vibrates,    vibrating,    vibration,    vice,    vicious,    viciously,    viciousness,    victimize,    vile,    vileness,    vilify,    villainous,    villainously,    villains,    vindictive,    vindictively,    vindictiveness,    violate,    violation,    violator,    violators,    violent,    violently,    viper,    virulence,    virulent,    virulently,    virus,    vociferous,    vociferously,    volatile,    volatility,    vomit,    vomited,    vomiting,    vomits,    vulgar,    vulnerable',
        'wail,    wallow,    wane,    waning,    wanton,    war-like,    warily,    wariness,    warlike,    warned,    warning,    warp,    warped,    wary,    washed-out,    waste,    wasted,    wasteful,    wastefulness,    wasting,    water-down,    watered-down,    wayward,    weak,    weaken,    weakening,    weaker,    weakness,    weaknesses,    weariness,    wearisome,    weary,    wedge,    weed,    weep,    weird,    weirdly,    wheedle,    whimper,    whine,    whining,    whiny,    whips,   wicked,    wickedly,    wickedness,    wild,    wildly,    wiles,    wilt,    wily,    wimpy,    wince,    wobble,    wobbled,    wobbles,    woe,    woebegone,    woeful,    woefully,    womanizer,    womanizing,    worn,    worried,    worriedly,    worrier,    worries,    worrisome,    worry,    worrying,    worryingly,    worse,    worsen,    worsening,    worst,    worthless,    worthlessly,    worthlessness,    wound,    wounds,    wrangle,    wrath,    wreak,    wreaked,    wreaks,    wreck,    wrest,    wrestle,    wretch,    wretched,    wretchedly,    wretchedness,    wrinkle,    wrinkled,    wrinkles,    writhe,    wrong,    wrongful,    wrongly,    wrought',
        'yawn', 'zap,    zapped,    zaps,    zealot,    zealous,    zealously,    zombie']
    # extract each word
    neg_list = [x.lower().split(sep=',    ') for x in neg]
    for line in neg_list:
        for word in line:
            word = re.sub("[^a-zA-Z0-9\s]+", "", word)
            negative_trie.insert(word)

    res = [] # contains array of 3 dictionary [[pos,neg,neu], [pos,neg,neu]... ]
    for idx in range(len(delivery_list)):
        list_ = []
        positive, negative, neutral = {},{},{}

        # Open the article file
        with open("../News/Cleaned/" + delivery_list[idx], encoding='utf-8') as f:
                list_ = f.readlines()

        # Remove unnecessary new lines
        for i in range(len(list_)):
            list_[i] = list_[i].strip()
            list_[i] = re.sub("[^a-zA-Z0-9\s]+", "", list_[i])
        list_ = list(filter(None, list_))

        # Count, find and delete stopwords
        for line in list_:
            for word in line.split():
                if positive_trie.search(word):
                    if word in positive:
                        positive[word] += 1
                    else:
                        positive[word] = 1
                elif negative_trie.search(word):
                    if word in negative:
                        negative[word] += 1
                    else:
                        negative[word] = 1
                else:
                    if word in neutral:
                        neutral[word] += 1
                    else:
                        neutral[word] = 1
        res.append([positive, negative, neutral])

    # sort the dictionary according to the occurance
    for company in res:
        for i in range(len(company)):
            company[i] = {k: v for k, v in sorted(company[i].items(), key=lambda item: item[1], reverse=True)}
    return res

"""
Histogram of Count of Stop Word against Company
"""
company_PNN_List = countWordTypes() # array of size 5, each element is a list of 3 dictionary, storing positive, negative, and neutral words-frequency
company = ['Company', 'City-Link', 'Pos Laju','GDex', 'J&T', 'DHL']
wordCount = ['Stop Word Count']
totalCount = ['Total Word Count']
wordCount.extend(findAndDeleteStopWords())

# Calculate the total word count for all of the companies
for idx in range (0,5):
    totalCount.append(len(company_PNN_List[idx][0])+len(company_PNN_List[idx][1])+len(company_PNN_List[idx][2]) + wordCount[idx+1])

# Save the result into a csv file
np.savetxt('stopword_company.csv', [p for p in zip(company, wordCount, totalCount)], delimiter=',', fmt='%s')

# Print out the result
df = pd.read_csv('stopword_company.csv')
print(df.head())

# Remove the element 'Company' from the array
wordCount.pop(0)
totalCount.pop(0)

# Display the chart
fig = go.Figure(data=[
    go.Bar(name='Stop Word Count', x=company_list, y=wordCount),
    go.Bar(name='Total Word Count', x=company_list, y=totalCount)
])

# Change the bar mode
fig.update_layout(barmode='group')
fig.show()

#Histogram of positive word and negative word count of each courier company
couriers=['City-Link', 'Pos Laju', 'Gdex', 'J&T', 'DHL']
data=[
    go.Bar(name='Positive', x=couriers, y=[len(countWordTypes()[0][0]),len(countWordTypes()[1][0]), len(countWordTypes()[2][0]), len(countWordTypes()[3][0]), len(countWordTypes()[4][0])]),
    go.Bar(name='Negative', x=couriers, y=[len(countWordTypes()[0][1]), len(countWordTypes()[1][1]), len(countWordTypes()[2][1]), len(countWordTypes()[3][1]), len(countWordTypes()[4][1])])
]
fig = go.Figure(data)

# Change the bar mode
fig.update_layout(barmode='group', title = "Positive and Negative Word Count of each courier company",  xaxis_title="Courier Company",
    yaxis_title="Word Count")
fig.show()


"""
To Sort Company According to Ranking/Reputation
"""
company_Reputation = []
for idx in range(0,5):
    company_Reputation.append(len(company_PNN_List[idx][0]) - 2*len(company_PNN_List[idx][1]))

company_to_score = {}
for i in range(len(company_Reputation)):
    company_to_score[company_list[i]] = company_Reputation[i]
company_to_score = {k: v for k, v in sorted(company_to_score.items(), key=lambda item: item[1], reverse=True)}

print('Company Ranking: ',end='')
for k, v in company_to_score.items():
    print(k, end="->")

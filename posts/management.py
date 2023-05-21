from .models import Post, Comment

def save_default(sender, **kwargs):
    data = [
        {
            'post': "For more than two decades, I've been immersed in the electrifying rhythm of the corporate world. I've embraced the relentless waves of strategic planning and leadership challenges, each one shaping me into the dedicated professional I am today. The thrill of success, the sting of setbacks, the invaluable lessons learned - all have been stepping stones on my journey.",
            'comments': []
        },
        {
            'post': "As I look back, I see a tapestry woven with threads of hard-earned successes, valuable lessons, and moments of growth. These are the threads that connect us all, stirring empathy and understanding, reminding me that we're not alone in our experiences. Each day is another opportunity to add to this tapestry, and I am filled with gratitude for this incredible journey.",
            'comments': []
        },
        {
            'post': "But, I've also witnessed the resilience of the human spirit in the face of adversity. The shared camaraderie during difficult times, the spark in the team's eyes when a problem was solved, the collective sigh of relief when a risk paid off - these are the moments that inspire me to do better, to be better.",
            'comments': []
        },
        {
            'post': "My experiences have etched unforgettable memories in my heart - from the first time I walked into my office as CEO, the nervous excitement palpable in the air, to the moments of shared triumph as our team achieved milestones we once thought unreachable.",
            'comments': []
        },
        {
            'post': "Starting as a wide-eyed Harvard Business School graduate, the road to becoming a CEO was paved with intense dedication, countless late-night strategizing, and the persistent pursuit of excellence. I've felt the weight of decision-making, the responsibility of leading a team, and the exhilaration of seeing a company evolve under my guidance.",
            'comments': []
        },
        {
            'post': "Each voyage out into the sea is an adventure, a dance with the elements. The exhilaration of a bountiful catch, the shared laughter and camaraderie with fellow fishermen, these are the moments that infuse life into my days. Yet, the sea is not always kind. There are memories of stormy nights, of battling against towering waves, of silent prayers whispered to the howling wind. These moments, testing and humbling, have forged my resolve and taught me the true meaning of resilience.",
            'comments': []
        },
        {
            'post': "Over the years, the sea has become my home, the rhythm of the tide syncing with my own heartbeat. The rising sun would often find me on my boat, casting my net into the vast, unpredictable ocean. There's a simple yet profound joy in feeling the cool morning breeze, hearing the caw of seagulls overhead, witnessing the world awaken to a new day.",
            'comments': []
        },
        {
            'post': "I remember the first time my father handed me a fishing rod, his weather-beaten hands guiding my inexperienced ones. The thrill of my first catch, the weight of the fish tugging at the line, is a feeling etched in my memory, as vivid now as it was then.",
            'comments': []
        },
        {
            'post': "As a seasoned fisherman, I've spent the better part of my life cradled by the ebb and flow of the sea. The gentle lull of the waves and the call of the distant horizon have been my faithful companions, shaping my existence in ways only a sailor could understand.",
            'comments': []
        },
        {
            'post': "As I set out each day, with the taste of salt in the air and the promise of the unknown ahead, I am more than a fisherman. I am a guardian of age-old traditions, a storyteller of the sea, a witness to the beautiful, unyielding dance between man and nature. My story is not just about fishing; it's a love letter to the sea, an homage to the simple yet profound life of a seafarer.",
            'comments': ["Your words resonate with a deep love and respect for the sea and your profession. The way you describe your experiences truly paints a vivid picture and gives us a glimpse of the unique life of a seafarer. It's inspiring to see how you embrace and honor these age-old traditions. Keep weaving these wonderful stories!", "This is such a beautiful reflection on your life as a fisherman. It's rare to find someone who can so eloquently articulate their connection with nature. You're not just a guardian of traditions, but also an advocate for respecting and understanding the delicate balance of our ecosystems. Thank you for sharing your journey.", "There's something profoundly touching about your story. The way you describe the 'dance between man and nature' makes me long for the simplicity and raw beauty of a life intertwined with the sea. It's refreshing to hear someone speak about their profession with such passion and reverence. You are a true storyteller of the sea."]
        },
        {
            'post': "Fishing is not just my livelihood; it's a testament to the ebbs and flows of life itself. The sea has taught me about patience, about respect for nature, about the delicate balance that sustains us. It has shown me the power of community, the shared triumphs and trials that bind us together.",
            'comments': ["This hits home! As a fellow fisherman, I can absolutely relate to your words. Fishing truly is a metaphor for life and its ever-changing nature. There's so much wisdom to be gained from the sea. It's a humbling and rewarding journey that binds us together as a community.", "It's touching to see how you've found deep life lessons in your daily work. The way you've captured the sea's teachings about patience, respect, and balance is so profound. It shows us how closely our lives are intertwined with nature, and the importance of acknowledging that connection."]
        },
        {
            'post': "As a seasoned fisherman, I've spent the better part of my life cradled by the ebb and flow of the sea. The gentle lull of the waves and the call of the distant horizon have been my faithful companions, shaping my existence in ways only a sailor could understand.",
            'comments': ["Your words paint a stunning picture of life at sea. It's evident how profoundly the ocean has shaped you. There's something deeply fascinating about the unique understanding and bond a sailor shares with the sea.", "As a fellow seafarer, I can deeply relate to your sentiments. The sea isn't just our workplace; it's our confidant, our constant, our muse. It truly shapes us in ways that are hard to put into words, but you've done an incredible job capturing it.", "Your narration is deeply poetic and evocative. The connection you share with the sea is palpable in your words. It's not often we see the profound impact of a profession on an individual's life narrated so eloquently.", "Reading your account makes me long for the sea and its endless mysteries. The way you talk about the ebb and flow of the sea, the distant horizon, and the lull of the waves, it's clear that being a fisherman isn't just a job for you, it's a lifestyle, a calling, an identity. It's truly inspiring."]
        },
    ]

    for sample in data:
        post = Post.objects.get_or_create(content=sample['post'])[0]
        for comment in sample['comments']:
            Comment.objects.get_or_create(post_id=post, content=comment)

    print('Default data saved')

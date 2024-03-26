from transformers import pipeline
import nltk
nltk.download('punkt') 
nltk.download('stopwords')
from collections import Counter 
from nltk.corpus import stopwords

from nltk.tokenize import sent_tokenize, word_tokenize

# def summarizer(text, min, max):
		# 1 : [30, 130], 
		# 2 : [100, 300],
		# 3 : [150, 400],
		# 4 : [200, 500]

text = """An eclipse is an astronomical event that occurs when an astronomical object or spacecraft is temporarily obscured, by passing into the shadow of another body or by having another body pass between it and the viewer. This alignment of three celestial objects is known as a syzygy.[1] An eclipse is the result of either an occultation (completely hidden) or a transit (partially hidden). A "deep eclipse" (or "deep occultation") is when a small astronomical object is behind a bigger one.[2][3] The term eclipse is most often used to describe either a solar eclipse, when the Moon's shadow crosses the Earth's surface, or a lunar eclipse, when the Moon moves into the Earth's shadow. However, it can also refer to such events beyond the Earth–Moon system: for example, a planet moving into the shadow cast by one of its moons, a moon passing into the shadow cast by its host planet, or a moon passing into the shadow of another moon. A binary star system can also produce eclipses if the plane of the orbit of its constituent stars intersects the observer's position. For the special cases of solar and lunar eclipses, these only happen during an "eclipse season", the two times of each year when the plane of the Earth's orbit around the Sun crosses with the plane of the Moon's orbit around the Earth and the line defined by the intersecting planes points near the Sun. The type of solar eclipse that happens during each season (whether total, annular, hybrid, or partial) depends on apparent sizes of the Sun and Moon. If the orbit of the Earth around the Sun and the Moon's orbit around the Earth were both in the same plane with each other, then eclipses would happen every month. There would be a lunar eclipse at every full moon, and a solar eclipse at every new moon. And if both orbits were perfectly circular, then each solar eclipse would be the same type every month. It is because of the non-planar and non-circular differences that eclipses are not a common event. Lunar eclipses can be viewed from the entire nightside half of the Earth. But solar eclipses, particularly total eclipses occurring at any one particular point on the Earth's surface, are very rare events that can be many decades apart.
The term is derived from the ancient Greek noun ἔκλειψις (ékleipsis), which means "the abandonment", "the downfall", or "the darkening of a heavenly body", which is derived from the verb ἐκλείπω (ekleípō) which means "to abandon", "to darken", or "to cease to exist,"[4] a combination of prefix ἐκ- (ek-), from preposition ἐκ (ek), "out," and of verb λείπω (leípō), "to be absent".[5][6] For any two objects in space, a line can be extended from the first through the second. The latter object will block some amount of light being emitted by the former, creating a region of shadow around the axis of the line. Typically these objects are moving with respect to each other and their surroundings, so the resulting shadow will sweep through a region of space, only passing through any particular location in the region for a fixed interval of time. As viewed from such a location, this shadowing event is known as an eclipse.[7]

Typically the cross-section of the objects involved in an astronomical eclipse is roughly disk-shaped.[7] The region of an object's shadow during an eclipse is divided into three parts:[8]

The umbra (Latin for "shadow"), within which the object completely covers the light source. For the Sun, this light source is the photosphere.
The antumbra (from Latin ante, "before, in front of", plus umbra) extending beyond the tip of the umbra, within which the object is completely in front of the light source but too small to completely cover it.
The penumbra (from the Latin paene, "almost, nearly", plus umbra), within which the object is only partially in front of the light source.

A total eclipse occurs when the observer is within the umbra, an annular eclipse when the observer is within the antumbra, and a partial eclipse when the observer is within the penumbra. During a lunar eclipse only the umbra and penumbra are applicable, because the antumbra of the Sun-Earth system lies far beyond the Moon. Analogously, Earth's apparent diameter from the viewpoint of the Moon is nearly four times that of the Sun and thus cannot produce an annular eclipse. The same terms may be used analogously in describing other eclipses, e.g., the antumbra of Deimos crossing Mars, or Phobos entering Mars's penumbra.

The first contact occurs when the eclipsing object's disc first starts to impinge on the light source; second contact is when the disc moves completely within the light source; third contact when it starts to move out of the light; and fourth or last contact when it finally leaves the light source's disc entirely.

For spherical bodies, when the occulting object is smaller than the star, the length (L) of the umbra's cone-shaped shadow is given by:

where Rs is the radius of the star, Ro is the occulting object's radius, and r is the distance from the star to the occulting object. For Earth, on average L is equal to 1.384×106 km, which is much larger than the Moon's semimajor axis of 3.844×105 km. Hence the umbral cone of the Earth can completely envelop the Moon during a lunar eclipse.[9] If the occulting object has an atmosphere, however, some of the luminosity of the star can be refracted into the volume of the umbra. This occurs, for example, during an eclipse of the Moon by the Earth—producing a faint, ruddy illumination of the Moon even at totality.

On Earth, the shadow cast during an eclipse moves very approximately at 1 km per sec. This depends on the location of the shadow on the Earth and the angle in which it is moving.[10]
"""
words = text.split(' ')
print("Word")

# sentences = sent_tokenize(text)
# print(len(sentences))

# if (len(sentences) >= 30) :
# 	n = 25 if len(sentences)%25 == 0 else len(sentences)%25

# 	stop_words = set(stopwords.words('english'))

# 	words = [word.lower() for word in word_tokenize(text) if word.lower() not in stop_words and word.isalnum()]

# 	word_freq = Counter(words)

# 	sentence_scores = {}

# 	for sentence in sentences:
# 		sentence_words = [word.lower() for word in word_tokenize(sentence) if word.lower() not in stop_words and word.isalnum()]
# 		sentence_score = sum([word_freq[word] for word in sentence_words])
# 		if len(sentence_words) < 20:
# 			sentence_scores[sentence] = sentence_score

# 	summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:n]
# 	text = ' '.join(summary_sentences)


# Retrieve the bart summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
sum_list = summarizer(text, max_length=int(max), min_length=int(min), do_sample=False) #, truncation=True)

# Input those variables into the summarizer
# sum_list = summarizer(text, do_sample=False, length_penalty = -0.5)

# Seperate the text out from its dictionary
summary = sum_list[0].get("summary_text")
print('Summary: ', summary)

# # # Sending back sentence
# # return summary

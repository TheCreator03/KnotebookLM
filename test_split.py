from split import split_text
from embed_and_store import add_documents

test_text = """

In the distant lands where the sky meets the earth in a hazy blend of purples and oranges, a tiny village nestled against the jagged cliffs that formed an unbroken chain stretching far into the horizon. The air, crisp and full of the scent of pine, carried whispers of secrets from long-forgotten times, and the echo of old stories floated through the branches of towering trees. Every evening, as the sun dipped below the cliffs, the villagers gathered by the river, its silver surface reflecting the fading light in soft ripples. There, they spoke of legends—some told with a quiet reverence, others with a burst of laughter. The tales were as varied as the stars in the sky, each one unique, yet all bound by the same thread of wonder and mystery.

The children played along the riverbanks, their laughter a bright, ringing sound that seemed to carry on the wind. They wove intricate patterns in the sand, leaving behind trails of their imagination that the river would gently erase as if it held the power to cleanse all that was temporary. The older folk, wise in the ways of the earth and sky, watched the children with a mixture of fondness and nostalgia, knowing that the future was being shaped by these small, fleeting moments.

Among the villagers was an old woman who had once been a traveler, her footsteps having touched the corners of the world. Her hair, silver as the moonlight that bathed the village at night, framed a face weathered by years of adventure. She was known to tell stories with such vivid detail that the listeners could almost feel the wind of distant lands in their hair, taste the salt of the sea, and hear the distant thunder of storms approaching from across the plains. Her tales spoke of places where the mountains kissed the clouds, where cities of glass and steel rose above endless deserts, and where dragons still roamed the skies, their wings beating like the pulse of the earth itself.

In the heart of the village stood a great oak tree, its bark gnarled and twisted, its roots deep in the earth, stretching far beneath the surface. The villagers believed the tree was ancient, older than any of them could comprehend, and that it held the memories of the land within its mighty trunk. Some said it had witnessed the rise and fall of empires, others claimed it was the keeper of time itself. On nights when the moon was full, the tree seemed to glow with an ethereal light, casting long shadows that danced like spirits around the village. It was under this tree that the village held its most important gatherings, where decisions were made, alliances were forged, and destinies were set.

The seasons passed, as they always did, and with each change, the village adapted. The spring brought renewal, with wildflowers blanketing the hillsides in a riot of colors, the summer brought warmth and abundance, the autumn brought harvest and reflection, and the winter brought stillness, a time for quiet contemplation and rest. The villagers understood the rhythm of the earth, and they lived in harmony with its cycles, taking only what was needed and giving back with gratitude.

But beyond the village, the world was changing. New lands were being discovered, and strange new peoples were beginning to appear on the shores of the distant seas. The winds carried tales of far-off kingdoms, their rulers both noble and tyrannical, their armies vast and powerful. The village, however, remained untouched by these forces. It was a place outside of time, a sanctuary where the past and future mingled, and the present was always just as it should be. Yet, as the days turned into years, the villagers began to wonder—how long could such a place remain untouched by the wider world? Would the winds of change eventually reach their shores, bringing with them both new opportunities and unknown dangers?

Only time would tell, and as the sun sank lower in the sky each evening, the villagers continued to gather by the river, telling stories, dreaming dreams, and savoring the quiet magic of their timeless home.

"""

user_id = '321'
document_id = '12345'
splits = split_text(test_text, user_id, document_id)
for split in splits:
    print (split.page_content[:50], split.metadata)

vector_ids = add_documents(splits)
# Example user and document ID, uses the "split_text" definition to print the page out/
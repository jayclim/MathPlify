## Inspiration/Problem
According to a 2019 survey by the National Association of Secondary School Principals, 63% of high school principals said their students felt unprepared for finals, and 57% of principals said that they had insufficient resources to provide enough practice problems for students. I also had a friend who was studying for finals and they didn't have enough practice problems and needed more. But the teacher did not have any more and it was difficult to find problems online, and we all know **Practice Makes Perfect!**

## What it does
Students can upload an image of a math problem, both word problems and problems with equations, and the website uses AI to read the problem/extract LaTeX. It then sends the problem to another AI model that will tweak it and generate more practice problems.

## How we built it
I used Python as a backend, Django as a web framework, Supabase to host a PostgreSQL database, and Vercel to host the website. For the AI models, I used MathPix's LaTeX extractor to read math problems and based the problem generator on the Bard LLM.

## Challenges we ran into
It was difficult hosting the website on Vercel since Django is not usually used with Vercel, caused a lot of errors and I spent a long time trying to fix the issues with Vercels read-only server (had to store temporary files in the /tmp directory). I also had a lot of issues with the AI's accuracy in generating problems and formatting them properly so a LaTeX renderer could understand them.

## Accomplishments that we're proud of
Getting the project done and mostly functioning :D. I thankfully encountered the Django Vercel issue before which allowed me to debug and fix the issue a lot quicker than before. I'm also proud of building a useful tool that works pretty well (and looks pretty!).

## What's next for MathPlify
Creating mobile apps powered by the same structure is probably the most important next step as it's much easier for students to snap a picture on their phone and upload/crop images locally. Improving the model's accuracy is also important as well since very complex problems can be quite tricky to generate more problems. Finally, after the product is polished, providing schools with this new tool can allow students to have unlimited practice so no one will have to be in the same situation as my friend.

#### Info
I am Jayden Lim, and I live in California, USA. You can contact me through my email sqwatato@gmail.com.

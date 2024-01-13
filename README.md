# Chapps
https://devpost.com/software/chapps
![gallery](https://github.com/ShinnosukeUesaka/chapps/assets/45286939/1e57f5ff-7f52-480f-be01-d6aaf53f690c)
![gallery (1)](https://github.com/ShinnosukeUesaka/chapps/assets/45286939/dc40c2aa-3b8c-4b2e-98cf-34fe7a14b6c7)



Create personalized software using our AI toolmaker. Build and edit reusable, shareable tools that contain domain knowledge and fit your needs. No technical skills are required, pure English.

## Key prompt
```
Your job is to create a Chapp based on the prompt below. Chapp is a tool or an app that runs on GPT-4.

Give me the all the variables neccesary to define the chapp.
A chapp has a title, description, short description inputs variables(all lowercase and use underscore for multiple words), instruction(prompt for gpt-4), example pair of inputs and outputs (must be markdown). All the input variables are string.
Strictly follow the example yaml format below, as it would be parsed programatically.

Example Input
I want a tool that gives me a definition of a word, and three example sentences based on a context provided.

Example Output

title: Word Context Definition and Example Builder

short_description: A tool for learning new words and their usage in a specific context.

description: |-
   This Chapp provides you the definition of a specific word and constructs three sentences using that word, based around a specific context provided by the user. It's a tool that can be handy for learning new words, enhancing your vocabulary, and understanding the usage of a word in a context effectively.

inputs:
  - name: word
    description: Enter the word you want to learn about and see used in sentences.
  - name: context
    description: Specify the context or theme within which you want to see the word used.
instruction: |-
  For the word "{word}", first provide a clear and concise definition. Then, based on the context of "{context}", create three unique sentences that correctly use and demonstrate the meaning of the word.

example:
  inputs:
    word: procrastinate
    context: school
  output: |-
    ## Definition
    Procrastinate means to delay or postpone action; put off doing something.
    ## Example Sentences:
    1. Many students tend to procrastinate when it comes to studying for exams, often leading to stress and poor performance.
    2. In school, procrastinating on assignments can result in late submissions and penalties.
    3. Despite knowing the importance of timely work, John often found himself procrastinating on his school projects.
```

## Inspiration
We face niche, personal problems all the time in our lives. Perhaps you want a tool that can format your essay in a specific way, proofread legal documents, or edit the emails you send to your professor. We had to wait for software companies to solve our problems, but what if we can create our own tools with AI? Inspired by the notable advancements in NLP, particularly with models like GPT-4, which provide a foundation for translating human intent expressed in natural language into personalized tools that can be reused and shared. This project aims to break down barriers that traditionally separate non-programmers from the ability to create software. Building on the concept of end-user programming, Chapps allows users to create software on a smaller, more personal scale as opposed to mass-produced, one-size-fits-all solutions. The idea of leveraging and building upon tools created by others introduces a collaborative aspect, promoting a shared ecosystem of tools and domain knowledge.

## What it does
Our project accepts natural language descriptions from users specifying the tools they wish to create or modify. We utilize language models to interpret user input and generate reusable software artifacts that can be saved, shared, and modified by the users on our platform. This allows for continuous improvement and editing of tools, encapsulating domain knowledge and user preferences over time. Users can make modifications to existing tools, personalizing them according to their specific requirements. Our product offers intuitive user interfaces for each tool, making them easy to use, and more memorable than chat interfaces.


- domain knowledge a therapist can create a chapp that uses his domain knowledge to analyze patient
- reusable tool professional email writing
- personal niche problem

highly customizable You can take all the chapps above and modify them according to your need. i.e. changing output format, and include new input fields



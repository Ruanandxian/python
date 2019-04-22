from nltk import word_tokenize,sent_tokenize,pos_tag
sentences=sent_tokenize("Google is one of the best companies in the world.I constantly google myself to see what I'm up to.")#按句子分割
nouns=['NN','NNS','NNP','NNPS']
for sentence in sentences:
    if "google" in sentence.lower():
        taggedWords=pos_tag(word_tokenize(sentence))#先分词，查询词性
        print(taggedWords)
#[('Google', 'NNP'), ('is', 'VBZ'), ('one', 'CD'), ('of', 'IN'), ('the', 'DT'), ('best', 'JJS'), ('companies', 'NNS'), ('in', 'IN'), ('the', 'DT'), ('world.I', 'NN'), ('constantly', 'RB'), ('google', 'VBZ'), ('myself', 'PRP'), ('to', 'TO'), ('see', 'VB'), ('what', 'WP'), ('I', 'PRP'), ("'m", 'VBP'), ('up', 'RB'), ('to', 'TO'), ('.', '.')]
        for word in taggedWords:
            if word[0].lower()=='google' and word[1] in nouns:#word[0]为单词，word[1]为词性
                print(sentences)
#include <stdio.h>
#include <stdlib.h>
static int  count_words(char const *s, char c)
{
    int result;
    int is_word;
    result = 0;
    is_word = 0;
    while (*s)
    {
        if (is_word == 0 && *s != c)
            is_word = 1;
        if (is_word && *s == c)
        {
            result++;
            is_word = 0;
        }
        s++;
    }
    if (is_word)
        result++;
    return (result);
}
static int  free_strs(char **sep, int word_locate)
{
    int locate;
    locate = -1;
    while (++locate < word_locate - 1)
        free(sep[locate]);
    return (1);
}
static int  get_sep_word(char **sep, char const *s, char c)
{
    int     word_size;
    int     word_locate;
    char    *start;
    word_size = 0;
    word_locate = 0;
    while (*s)
    {
        if (word_size == 0 && *s != c)
            start = (char *)s;
        if (word_size && *s == c)
        {
            sep[word_locate] = ft_substr(start, 0, word_size);
            if (sep[word_locate++] == NULL)
                return (free_strs(sep, word_locate));
            word_size = 0;
        }
        if (*s != c)
            word_size++;
        s++;
    }
    if (word_size)
        sep[word_locate++] = ft_substr(start, 0, word_size);
    sep[word_locate] = NULL;
    return (0);
}
char    **ft_split(char const *s, char c)
{
    int     words;
    char    **result;
    if (!s)
        return (NULL);
    words = count_words(s, c);
    result = (char **)malloc(sizeof(char *) * (words + 1));
    if (result && get_sep_word(result, s, c))
    {
        free(result);
        result = NULL;
    }
    return (result);
}
int main() {
    char *test = "abc de f";
    char **test1;
    test1 = ft_split(test, ' ');
    int i = 0;
    while (test1[i]) {
        printf("%s\n", test1[i]);
    };
}
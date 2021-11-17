static char	*isUsed(char c, char	*start, char *end)
{
	while (start <= end)
	{
		end--;
		if (c == *end)
			return end;
	}
	return 0;
}

int lengthOfLongestSubstring(char * s){
	char	*start = s, *end = s;
	char	*tmp;
	size_t		maxSubstring = 0;

	while (*end)
	{
		tmp = isUsed(*end, start, end);
		if (!tmp)
			continue;
		else
			start = tmp + 1;
		end++;
		maxSubstring = maxSubstring > end - start ? maxSubstring : end - start;
	}
	return maxSubstring;
}

// https://leetcode.com/problems/design-hashmap/
#define HASHMAPSIZE 10000000

typedef struct		myhash
{
	char			occupied;
	int				value;
	//struct myhash	*next;
}				MyHashMap;


MyHashMap* myHashMapCreate() {
	MyHashMap *ret;

	ret = malloc(sizeof(MyHashMap) * HASHMAPSIZE);
	for (int i = 0; i < HASHMAPSIZE; i++)
		ret[i].occupied = 0;
	return ret;
}

void myHashMapPut(MyHashMap* obj, int key, int value)
{
	MyHashMap	*tmp;

	obj[key].value = value;
	obj[key].occupied = 1;
	//tmp = &obj[key];
	//if (!tmp->occupied)
	//{
	//	tmp->occupied = 1;
	//	tmp->value = value;
	//	tmp->next = 0;
	//}
	//else
	//{
	//	while (tmp)
	//		tmp = tmp->next;
	//	tmp = malloc(sizeof(MyHashMap));
	//	tmp->value = value;
	//	tmp->next = 0;
	//}
}

int myHashMapGet(MyHashMap* obj, int key)
{
	if (!obj[key].occupied)
		return -1;
	return obj[key].value;
}

void myHashMapRemove(MyHashMap* obj, int key)
{
	obj[key].occupied = 0;
}

void myHashMapFree(MyHashMap* obj)
{
	free(obj);
}

/**
 * Your MyHashMap struct will be instantiated and called as such:
 * MyHashMap* obj = myHashMapCreate();
 * myHashMapPut(obj, key, value);
 
 * int param_2 = myHashMapGet(obj, key);
 
 * myHashMapRemove(obj, key);
 
 * myHashMapFree(obj);
*/
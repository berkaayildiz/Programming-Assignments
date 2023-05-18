package implementations;

import interfaces.ListInterface;

/**
 * An array-based implementation of the ListInterface.
 */
public final class ArrayList<T> implements ListInterface<T>
{
    private T[] list;
    private int size;
    private boolean initialized = false;
    private static final int DEFAULT_CAPACITY = 50;
    private static final int MAX_CAPACITY = 10000;

    public ArrayList()
    {
       this(DEFAULT_CAPACITY);
    }

    public ArrayList(int initialCapacity)
    {
        checkCapacity(initialCapacity);

        // The cast is safe because the new array contains null entries
        @SuppressWarnings("unchecked")
        T[] tempList = (T[]) new Object[DEFAULT_CAPACITY];
        list = tempList;

        size = 0;
        initialized = true;
    }

    public boolean add(T newEntry)
    {   
        checkInitialization();
        ensureCapacity();
        list[size] = newEntry;
        size++;
        return true;
    }

    public void add(int index, T newEntry)
    {   
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException();
        }

        checkInitialization();
        ensureCapacity();

        System.arraycopy(list, index, list, index + 1, size - index);
        list[index] = newEntry;
        size++;
    }

    public T get(int index)
    {
        checkInitialization();
        
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException();
        }

        return list[index];
    }

    public T remove(int index)
    {
        checkInitialization();

        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException();
        }
        T removed = list[index];
        System.arraycopy(list, index + 1, list, index, size - index - 1); // removes the entry and shifts the rest of the list
        size--;
        list[size] = null;

        return removed;
    }

    public boolean remove(T newEntry)
    {
        checkInitialization();
    
        for (int i = 0; i < size; i++) {
            if (newEntry == null ? list[i] == null : newEntry.equals(list[i])) {
                remove(i);
                return true;
            }
        }
    
        return false;
    }

    public T set(int index, T newEntry)
    {
        checkInitialization();

        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException();
        }
        T replaced = list[index];
        list[index] = newEntry;
        return replaced;
    }

    public boolean contains(Object o)
    {
        for (int i = 0; i < size; i++)
        {
            if (o == null ? list[i] == null : o.equals(list[i])) {
                return true;
            }
        }
        return false;
    }
    
    public int size()
    {
        return size;
    }

    public boolean isEmpty()
    {
        return size == 0;
    }

    private void ensureCapacity() 
    {
        if (size == list.length)
        {
            T[] oldList = list;
            int oldSize = oldList.length;
            int newSize = oldSize * 2;

            checkCapacity(newSize);

            // The cast is safe because the new array contains null entries
            @SuppressWarnings("unchecked")
            T[] tempList = (T[]) new Object[newSize];
            list = tempList;
            for (int index = 0; index < oldSize; index++)
            {
                list[index] = oldList[index];
            }
        }
    }
    
    private void checkInitialization() throws SecurityException
    {
        if (!initialized)
        {
            throw new SecurityException("ArrayList object is not initialized properly.");
        }
    }

    private void checkCapacity(int capacity) throws IllegalStateException
    {
        if (capacity > MAX_CAPACITY)
        {
            throw new IllegalStateException("Attempt to create a list whose capacity exceeds allowed maximum.");
        }
    }
}

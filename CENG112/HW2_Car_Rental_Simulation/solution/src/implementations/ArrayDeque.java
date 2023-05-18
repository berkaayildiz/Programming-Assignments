package implementations;

import java.util.NoSuchElementException;

import interfaces.DequeInterface;

/**
 * An array-based implementation of the DequeInterface.
 */
public final class ArrayDeque<T> implements DequeInterface<T> {
    
    private T[] deque;
    private int frontIndex;
    private int backIndex;
    private int size;
    private boolean initialized = false;
    private static final int DEFAULT_CAPACITY = 50;
    private static final int MAX_CAPACITY = 10000;

    public ArrayDeque()
    {
        this(DEFAULT_CAPACITY);
    }

    public ArrayDeque(int initialCapacity)
    {      
        @SuppressWarnings("unchecked")
        T[] tempDeque = (T[]) new Object[initialCapacity];
        deque = tempDeque;

        frontIndex = 0;
        backIndex = initialCapacity - 1;
        size = 0;
        initialized = true;
    }

    public void addToFront(T newEntry)
    {
        checkInitialization();
        ensureCapacity();
        frontIndex = (frontIndex - 1 + deque.length) % deque.length;
        deque[frontIndex] = newEntry;
        size++;
    }

    public void addToBack(T newEntry)
    {
        checkInitialization();
        ensureCapacity();
        backIndex = (backIndex + 1) % deque.length;
        deque[backIndex] = newEntry;
        size++;
    }

    public T removeFront()
    {
        checkInitialization();

        if (isEmpty())
        {
            throw new NoSuchElementException();
        }

        T front = deque[frontIndex];
        deque[frontIndex] = null;
        frontIndex = (frontIndex + 1) % deque.length;
        size--;

        return front;
    }

    public T removeBack()
    {
        checkInitialization();

        if (isEmpty())
        {
            throw new NoSuchElementException();
        }

        T back = deque[backIndex];
        deque[backIndex] = null;
        backIndex = (backIndex - 1 + deque.length) % deque.length;
        size--;

        return back;
    }

    public T getFront()
    {
        checkInitialization();

        if (isEmpty())
        {
            throw new NoSuchElementException();
        }

        return deque[frontIndex];
    }

    public T getBack()
    {
        checkInitialization();

        if (isEmpty()) 
        {
            throw new NoSuchElementException();
        }

        return deque[backIndex];
    }

    public boolean isEmpty() 
    {
        return size == 0;
    }

    public void clear()
    {
        @SuppressWarnings("unchecked")
        T[] tempDeque = (T[]) new Object[DEFAULT_CAPACITY];
        deque = tempDeque;
        frontIndex = 0;
        backIndex = DEFAULT_CAPACITY - 1;
        size = 0;
    }

    public int size()
    {
        return size;
    }

    private void ensureCapacity()
    {
        if (frontIndex == ((backIndex + 2) % deque.length))
        {
            T[] oldDeque = deque;
            int oldSize = oldDeque.length;
            int newSize = 2 * oldSize;

            checkCapacity(newSize);
            
            // The cast is safe because the new array contains null entries
            @SuppressWarnings("unchecked")
            T[] tempDeque = (T[]) new Object[newSize];
            deque = tempDeque;

            for (int i = 0; i < oldSize - 1; i++) {
                deque[i] = oldDeque[frontIndex];
                frontIndex = (frontIndex + 1) % oldSize;
            }
            frontIndex = 0;
            backIndex = oldSize - 2;
        }
    }

    private void checkInitialization() throws SecurityException
    {
        if (!initialized)
        {
            throw new SecurityException("ArrayQueue object is not initialized properly.");
        }
    }

    private void checkCapacity(int capacity) throws IllegalStateException
    {
        if (capacity > MAX_CAPACITY)
        {
            throw new IllegalStateException("Attempt to create a queue whose capacity exceeds allowed maximum.");
        }
    }
}

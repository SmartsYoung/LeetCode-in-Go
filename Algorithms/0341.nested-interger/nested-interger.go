package _341_nested_interger

// This is the interface that allows for creating nested lists.
// You should not implement it, or speculate about its implementation
type NestedInteger struct {
}

// Return true if this NestedInteger holds a single integer, rather than a nested list.
func (this NestedInteger) IsInteger() bool {
	return false
}

// Return the single integer that this NestedInteger holds, if it holds a single integer
// The result is undefined if this NestedInteger holds a nested list
// So before calling this method, you should have a check
func (this NestedInteger) GetInteger() int {
	return 0
}

// Set this NestedInteger to hold a single integer.
func (n *NestedInteger) SetInteger(value int) {}

// Set this NestedInteger to hold a nested list and adds a nested integer to it.
func (this *NestedInteger) Add(elem NestedInteger) {}

// Return the nested list that this NestedInteger holds, if it holds a nested list
// The list length is zero if this NestedInteger holds a single integer
// You can access NestedInteger's List element directly if you want to modify it
func (this NestedInteger) GetList() []*NestedInteger {
	return []*NestedInteger{}
}

type NestedIterator struct {
	Data []*NestedInteger
}

func Constructor(nestedList []*NestedInteger) *NestedIterator {
	m := &NestedIterator{Data: nestedList}
	return m
}

func (this *NestedIterator) Next() int {
	v := this.Data[0].GetInteger()
	this.Data = this.Data[1:]
	return v
}

func (this *NestedIterator) HasNext() bool {
	if len(this.Data) == 0 {
		return false
	}
	if this.Data[0].IsInteger() {
		return true
	}
	this.Data = append(this.Data[0].GetList(), this.Data[1:]...)
	return this.HasNext()
}

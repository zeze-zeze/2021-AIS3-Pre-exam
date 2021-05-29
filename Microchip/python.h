#include <fstream>
#include <iostream>
#include <vector>


using std::ios;
using std::string;
using std::vector;


struct str : public string {
    template <typename... T> str(T &&...t) : string(std::forward<T>(t)...) {}
    operator int() {
        return std::stoi(*this);
    }
    str strip() const {
        auto first = begin(), last = end();
        auto is_whitespace = [](const char &c) {
            return c == ' ' || c == '\t' || c == '\n' || c == '\r';
        };
        while (first != last && is_whitespace(*first))
            ++first;
        while (first != last && is_whitespace(*(last - 1)))
            --last;
        return str(first, last);
    }
};

struct open {
    std::fstream file;
    open(const string &filename, const string &mode = "r") {
        ios::openmode file_mode = ios::openmode(0);
        for (char c : mode) {
            switch (c) {
            case 'r': file_mode |= ios::in; break;
            case 'w': file_mode |= ios::out | ios::trunc; break;
            case 'b': file_mode |= ios::binary; break;
            case 'a': file_mode |= ios::out | ios::app; break;
            }
        }
        file.exceptions(ios::failbit);
        file.open(filename, file_mode);
    }
    ~open() {
        if (file.is_open())
            file.close();
    }
    str read(size_t size = SIZE_MAX) {
        if (size == SIZE_MAX) {
            auto pos = file.tellg();
            file.seekg(0, ios::end);
            size = file.tellg() - pos;
            file.seekg(pos);
        }
        string res(size, '\0');
        file.read(&res[0], size);
        return res;
    }
    size_t write(const string &s) {
        file.write(s.data(), s.size());
        return s.size();
    }
};

template <typename value_type = int> struct range_t {
    struct iterator {
        value_type value, step;
        iterator &operator++() {
            value += step;
            return *this;
        }
        iterator operator++(int) {
            auto old = std::copy(*this);
            value += step;
            return old;
        }
        const value_type &operator*() const {
            return value;
        }
        bool operator==(const iterator &other) const {
            return value == other.value && step == other.step;
        }
        bool operator!=(const iterator &other) const {
            return !(*this == other);
        }
    };
    iterator it_begin, it_end;

    range_t(value_type stop) : range_t(0, stop, 1) {}
    range_t(value_type start, value_type stop, value_type step = 1) {
        if (!step)
            throw std::invalid_argument("step must be non-zero");

        if (step > 0) {
            if (stop < start)
                stop = start;
            else
                stop = start + (stop - start + step - 1) / step * step;
        } else {
            if (stop > start)
                stop = start;
            else
                stop = start + (start - stop - step - 1) / (-step) * step;
        }
        it_begin = iterator{start, step}, it_end = iterator{stop, step};
    }
    iterator begin() const {
        return it_begin;
    }
    iterator end() const {
        return it_end;
    }
};

using range = range_t<int>;


template <typename value_type = int> struct list_t : public vector<value_type> {
    template <typename... T>
    list_t(T &&...t) : vector<value_type>(std::forward<T>(t)...) {}
    void append(const value_type &value) {
        this->push_back(std::forward<value_type>(value));
    }
    void append(value_type &&value) {
        this->push_back(std::forward<value_type>(value));
    }
};

using list = list_t<int>;


template <typename T> void print(T t) {
    std::cout << t << std::endl;
}
template <typename T, typename... U> void print(T t, U... u) {
    std::cout << t << ' ';
    print(u...);
}

template <typename T> size_t len(const T &t) {
    return t.size();
}

int ord(const char &c) {
    return static_cast<int>(c);
}

char chr(const int &o) {
    if (o < 0 || o > 127)
        throw std::invalid_argument("order should be a valid ascii number");

    return static_cast<char>(o);
}

str input(const str &prompt = "") {
    std::cout << prompt << std::flush;
    str result;
    std::getline(std::cin, result);
    return result;
}


#define ꞉
#define if    if (
#define for   for (auto
#define in    :
#define elif  else if
#define def   auto
#define pass  ;
#define is    ==
#define None  NULL
#define True  true
#define False false


// variables
int temp, num;
list keys, nums;
str padded, result;

// magic arguments
// abusing weird c++ grammar rules
#define ARG(type, arg) type(arg)
#define name           ARG(str, name)
#define id             ARG(int, id)

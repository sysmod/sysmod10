.phony: all full svm scc python cpp java csharp

SUBDIRS = action_harel_ext \
          final_harel_ext \
          final_harel_nonext \
          history_harel_nonext \
          history_nonharel_nonext \
          importation_harel_ext \
          importation_harel_nonext \
          priority_harel_nonext \
          priority_nonharel_nonext \
          states_harel_nonext \
          states_nonharel_nonext \
          time_harel_ext \
          time_nonharel_ext

NEEDCOPY = final_harel_ext \
           history_nonharel_nonext \
           importation_harel_ext \
           priority_nonharel_nonext \
           states_nonharel_nonext \
           time_nonharel_ext

NEEDCOPY_JAVA_CSHARP = history_nonharel_nonext \
                       priority_nonharel_nonext \
                       states_nonharel_nonext

all:
	for dir in $(SUBDIRS); do \
	  if ! $(MAKE) -C $$dir all; then \
	    exit 1; \
	  fi; \
	done

full:
	for dir in $(SUBDIRS); do \
	  if ! $(MAKE) -C $$dir full; then \
	    exit 1; \
	  fi; \
	done

svm: precopy
	for dir in $(SUBDIRS); do \
	  if ! $(MAKE) -C $$dir svm; then \
	    exit 1; \
	  fi; \
	done
	for copydir in $(NEEDCOPY); do \
	  if ! $(MAKE) -C $$copydir clean; then \
	    exit 1; \
	  fi; \
	done

scc: precopy
	for dir in $(SUBDIRS); do \
	  if ! $(MAKE) -C $$dir scc; then \
	    exit 1; \
	  fi; \
	done
	for copydir in $(NEEDCOPY); do \
	  if ! $(MAKE) -C $$copydir clean; then \
	    exit 1; \
	  fi; \
	done

python: precopy
	for dir in $(SUBDIRS); do \
	  if ! $(MAKE) -C $$dir python; then \
	    exit 1; \
	  fi; \
	done
	for copydir in $(NEEDCOPY); do \
	  if ! $(MAKE) -C $$copydir clean; then \
	    exit 1; \
	  fi; \
	done

cpp: precopy
	for dir in $(SUBDIRS); do \
	  if ! $(MAKE) -C $$dir cpp; then \
	    exit 1; \
	  fi; \
	done
	for copydir in $(NEEDCOPY); do \
	  if ! $(MAKE) -C $$copydir clean; then \
	    exit 1; \
	  fi; \
	done

java: precopy_java_csharp
	for dir in $(SUBDIRS); do \
	  if ! $(MAKE) -C $$dir java; then \
	    exit 1; \
	  fi; \
	done
	for copydir in $(NEEDCOPY_JAVA_CSHARP); do \
	  if ! $(MAKE) -C $$copydir clean; then \
	    exit 1; \
	  fi; \
	done

csharp: precopy_java_csharp
	for dir in $(SUBDIRS); do \
	  if ! $(MAKE) -C $$dir csharp; then \
	    exit 1; \
	  fi; \
	done
	for copydir in $(NEEDCOPY_JAVA_CSHARP); do \
	  if ! $(MAKE) -C $$copydir clean; then \
	    exit 1; \
	  fi; \
	done

precopy:
	for copydir in $(NEEDCOPY); do \
	  if ! $(MAKE) -C $$copydir copy; then \
	    exit 1; \
	  fi; \
	done

precopy_java_csharp:
	for copydir in $(NEEDCOPY_JAVA_CSHARP); do \
	  if ! $(MAKE) -C $$copydir copy; then \
	    exit 1; \
	  fi; \
	done
